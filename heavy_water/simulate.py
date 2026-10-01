"""Heavy-water (D2O) mutation-accumulation experiment: simulation and power analysis.

Question: what fraction f_q of spontaneous transition mutations comes from
proton tunneling in DNA base pairs (Lowdin tautomers)?

Design simulated here (see ../heavy-water-experiment.md for the full protocol):
  * E. coli mutL (mismatch-repair deficient), so replication errors, including
    tautomer-induced ones, become mutations instead of being repaired.
  * Mutation-accumulation (MA) lines grown in media with D2O fraction x and at
    several temperatures, then whole-genome sequenced.
  * Each mutation is classified as a transition (ts, where tautomers act) or a
    transversion (tv, internal control that carries the classical solvent
    isotope effect but no tautomer signal).

Key idea: within one condition, generation counts, growth slowdown in D2O and
any isotope effect shared by ts and tv cancel in the ts:tv odds, so

    odds(x, T) = theta_T * h(x),   h(x) = 1 - f_T * x * (1 - rho),

where rho = P_D / P_H is the tunneling suppression from the WKB formula.
Tunneling is temperature-independent; classical chemistry is not. That
difference is the second, independent check on any non-zero f_q.

Run:  python simulate.py            (full run, ~1-2 min)
      python simulate.py --quick    (fewer power-analysis repeats)
"""
import argparse, json, pathlib
from dataclasses import dataclass, field, replace

import numpy as np
from scipy.optimize import curve_fit, minimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(__file__).parent
HBAR = 1.054571817e-34      # J s
AMU = 1.66053907e-27        # kg
EV = 1.602176634e-19        # J
KB_EV = 8.617333262e-5      # eV / K
M_H, M_D = 1.007276 * AMU, 2.013553 * AMU   # proton, deuteron
T_REF = 310.15                              # 37 C


# --- physics -----------------------------------------------------------------

def wkb_probability(barrier_ev, width_nm, mass):
    """Tunneling probability through a rectangular barrier, P = exp(-2 kappa d)."""
    kappa = np.sqrt(2 * mass * barrier_ev * EV) / HBAR
    return np.exp(-2 * kappa * width_nm * 1e-9)


def classical_isotope_factor(x, temp_k, delta_e_ev):
    """Rate multiplier from a zero-point-energy isotope effect when a fraction x
    of exchangeable protons is deuterated (linear proton inventory)."""
    return 1 + x * (np.exp(-delta_e_ev / (KB_EV * temp_k)) - 1)


# --- model of the world -----------------------------------------------------

@dataclass
class Truth:
    f_q: float = 0.10            # quantum share of transitions at 37 C, in H2O
    barrier_ev: float = 0.40     # illustrative double-well barrier for proton transfer
    width_nm: float = 0.05       # illustrative barrier width
    u_ts: float = 0.035          # transitions / genome / generation at 37 C (mutL)
    u_tv: float = 0.002          # transversions / genome / generation at 37 C (mutL)
    ea_ev: float = 0.50          # Arrhenius energy of classical mutation processes
    de_shared_ev: float = 0.010  # classical isotope effect on steps every mutation passes
                                 # through (polymerase, proofreading, dNTP pools)
    de_ts_extra_ev: float = 0.0  # extra classical isotope effect on transitions only
                                 # (e.g. over-barrier tautomerization); > 0 is the confound
    line_cv: float = 0.10        # line-to-line variation in overall mutation rate

    @property
    def rho(self):
        return (wkb_probability(self.barrier_ev, self.width_nm, M_D)
                / wkb_probability(self.barrier_ev, self.width_nm, M_H))

    def rates(self, x, temp_k):
        """Expected (ts, tv) mutations per genome per generation."""
        arrhenius = np.exp(-self.ea_ev / KB_EV * (1 / temp_k - 1 / T_REF))
        shared = classical_isotope_factor(x, temp_k, self.de_shared_ev)
        ts_extra = classical_isotope_factor(x, temp_k, self.de_ts_extra_ev)
        ts_classical = (1 - self.f_q) * arrhenius * ts_extra
        ts_quantum = self.f_q * (1 - x + x * self.rho)   # tunneling: no T dependence
        return self.u_ts * (ts_classical + ts_quantum) * shared, self.u_tv * arrhenius * shared


@dataclass
class Design:
    x_levels: tuple = (0.0, 0.5, 0.9)   # extremes carry the information; 0.5 checks linearity
    temps_c: tuple = (25.0, 37.0, 42.0)
    lines: int = 100              # MA lines per (x, T) condition
    generations: int = 3000       # generations per line
    gen_error_cv: float = 0.03    # error in measured generation counts per condition

    @property
    def temps_k(self):
        return tuple(t + 273.15 for t in self.temps_c)


def simulate(truth, design, rng):
    """Mutation counts per line: arrays of shape (n_x, n_T, lines)."""
    nx, nt = len(design.x_levels), len(design.temps_k)
    ts = np.zeros((nx, nt, design.lines), int)
    tv = np.zeros_like(ts)
    gens_measured = np.zeros((nx, nt))
    shape = 1 / truth.line_cv ** 2
    for i, x in enumerate(design.x_levels):
        for j, temp in enumerate(design.temps_k):
            r_ts, r_tv = truth.rates(x, temp)
            line_mult = rng.gamma(shape, 1 / shape, design.lines)
            ts[i, j] = rng.poisson(r_ts * design.generations * line_mult)
            tv[i, j] = rng.poisson(r_tv * design.generations * line_mult)
            gens_measured[i, j] = design.generations * (1 + rng.normal(0, design.gen_error_cv))
    return ts, tv, gens_measured


# --- analysis ----------------------------------------------------------------

def _nll(params, x, ts, tv, rho):
    log_theta, f = params
    h = 1 - f * x * (1 - rho)
    if np.any(h <= 0):
        return 1e12
    odds = np.exp(log_theta) * h
    p = odds / (1 + odds)
    return -np.sum(ts * np.log(p) + tv * np.log1p(-p))


def _hessian(fun, p, eps=1e-4):
    n = len(p)
    hess = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            pp = [np.array(p, float) for _ in range(4)]
            pp[0][a] += eps; pp[0][b] += eps
            pp[1][a] += eps; pp[1][b] -= eps
            pp[2][a] -= eps; pp[2][b] += eps
            pp[3][a] -= eps; pp[3][b] -= eps
            hess[a, b] = (fun(pp[0]) - fun(pp[1]) - fun(pp[2]) + fun(pp[3])) / (4 * eps * eps)
    return hess


def fit_fq(design, ts, tv, rho):
    """Per-temperature ML estimate of f_q from ts:tv odds, with a quasi-binomial
    standard error (inflated by line-level overdispersion)."""
    x = np.array(design.x_levels)
    results = []
    for j in range(len(design.temps_k)):
        ts_j, tv_j = ts[:, j].sum(1), tv[:, j].sum(1)
        theta0 = np.log(max(ts_j[0], 1) / max(tv_j[0], 1))
        fun = lambda p: _nll(p, x, ts_j, tv_j, rho)
        res = minimize(fun, [theta0, 0.0], method="Nelder-Mead",
                       options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 4000})
        cov = np.linalg.pinv(_hessian(fun, res.x))
        # overdispersion from line-level Pearson residuals
        odds = np.exp(res.x[0]) * (1 - res.x[1] * x * (1 - rho))
        p = (odds / (1 + odds))[:, None]
        n = ts[:, j] + tv[:, j]
        mask = n > 0
        chi2 = (((ts[:, j] - n * p) ** 2) / (n * p * (1 - p)))[mask].sum()
        phi = max(1.0, chi2 / (mask.sum() - 2))
        results.append({"f": res.x[1], "se": float(np.sqrt(max(cov[1, 1], 0) * phi)), "phi": phi})
    return results


def combined_test(design, ts, tv, rho):
    """One f_q shared across temperatures (a free ts:tv baseline per temperature),
    tested against f_q = 0 with a signed-root likelihood-ratio statistic.
    Returns (f_hat, se, z); z > 1.645 is a one-sided 5 % detection."""
    x = np.array(design.x_levels)
    nt = len(design.temps_k)
    ts_c, tv_c = ts.sum(2), tv.sum(2)                     # (n_x, n_T)

    def nll(p):
        return sum(_nll([p[j], p[-1]], x, ts_c[:, j], tv_c[:, j], rho) for j in range(nt))

    theta0 = [np.log(max(ts_c[:, j].sum(), 1) / max(tv_c[:, j].sum(), 1)) for j in range(nt)]
    best = minimize(nll, theta0 + [0.0], method="Nelder-Mead",
                    options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 8000})
    null = nll(theta0 + [0.0])                            # closed-form MLE when f = 0
    # overdispersion from line-level Pearson residuals under the full fit
    chi2, n_obs = 0.0, 0
    for j in range(nt):
        odds = np.exp(best.x[j]) * (1 - best.x[-1] * x * (1 - rho))
        p = (odds / (1 + odds))[:, None]
        n = ts[:, j] + tv[:, j]
        m = n > 0
        chi2 += (((ts[:, j] - n * p) ** 2) / (n * p * (1 - p)))[m].sum()
        n_obs += m.sum()
    phi = max(1.0, chi2 / (n_obs - nt - 1))
    f_hat = float(best.x[-1])
    z = float(np.sign(f_hat) * np.sqrt(max(2 * (null - best.fun), 0) / phi))
    cov = np.linalg.pinv(_hessian(nll, best.x))
    return f_hat, float(np.sqrt(max(cov[-1, -1], 0) * phi)), z


def temperature_signature(design, tv, gens_measured, per_t):
    """Tunneling is temperature-independent while classical mutation rises with
    T, so a real quantum share must FALL with temperature:
        f_T = F / (F + (1 - F) * exp(-E_a / k * (1/T - 1/T_ref))).
    A classical, transition-only isotope effect instead gives a roughly flat f_T.
    E_a is measured from the absolute transversion rates in H2O. Returns the
    observed weighted slope df/dT and the slope tunneling predicts (per K)."""
    temps = np.array(design.temps_k)
    f_t = np.array([r["f"] for r in per_t])
    f_se = np.array([r["se"] for r in per_t])
    mu_tv = tv[0].sum(1) / (design.lines * gens_measured[0])
    ea = -np.polyfit(1 / (KB_EV * temps), np.log(mu_tv), 1)[0]
    arr = np.exp(-ea / KB_EV * (1 / temps - 1 / T_REF))
    pred = lambda big_f: big_f / (big_f + (1 - big_f) * arr)
    w = 1 / f_se ** 2
    big_f = minimize(lambda p: np.sum(w * (f_t - pred(np.clip(p[0], 1e-6, 0.999))) ** 2),
                     [0.1], method="Nelder-Mead").x[0]
    big_f = float(np.clip(big_f, 1e-6, 0.999))
    t_bar = np.sum(w * temps) / w.sum()
    slope = float(np.sum(w * (temps - t_bar) * f_t) / np.sum(w * (temps - t_bar) ** 2))
    slope_se = float(1 / np.sqrt(np.sum(w * (temps - t_bar) ** 2)))
    pred_curve = pred(big_f)
    pred_slope = float(np.sum(w * (temps - t_bar) * pred_curve) / np.sum(w * (temps - t_bar) ** 2))
    return {"ea_ev": float(ea), "F_tunnel_fit": big_f, "slope": slope, "slope_se": slope_se,
            "tunnel_pred_slope": pred_slope, "f_T": f_t.tolist(), "f_T_se": f_se.tolist()}


# --- experiments ---------------------------------------------------------------

def run_scenario(name, truth, design, seed):
    rng = np.random.default_rng(seed)
    ts, tv, gens = simulate(truth, design, rng)
    per_t = fit_fq(design, ts, tv, truth.rho)
    f_hat, se, z = combined_test(design, ts, tv, truth.rho)
    return {"name": name, "true_f": truth.f_q, "f_hat": f_hat, "se": se, "z": z,
            "per_T": per_t, "temperature": temperature_signature(design, tv, gens, per_t),
            "ts": ts, "tv": tv}


def power_analysis(truth, design, f_values, line_counts, reps, seed):
    rng = np.random.default_rng(seed)
    table = {}
    for f in f_values:
        for n in line_counts:
            t, d = replace(truth, f_q=f), replace(design, lines=n)
            hits, estimates = 0, []
            for _ in range(reps):
                ts, tv, _ = simulate(t, d, rng)
                f_hat, se, z = combined_test(d, ts, tv, t.rho)
                hits += z > 1.645          # one-sided test at 5 %
                estimates.append(f_hat)
            table[(f, n)] = {"power": hits / reps, "mean_f_hat": float(np.mean(estimates))}
    return table


# --- figures -------------------------------------------------------------------

def plot_physics(truth):
    widths = np.linspace(0.02, 0.08, 100)
    fig, ax = plt.subplots(figsize=(6, 3.6))
    for barrier, style in [(0.3, ":"), (0.4, "-"), (0.5, "--")]:
        ax.semilogy(widths, wkb_probability(barrier, widths, M_H), "C0" + style, label=f"H, V={barrier} eV")
        ax.semilogy(widths, wkb_probability(barrier, widths, M_D), "C3" + style, label=f"D, V={barrier} eV")
    ax.axvline(truth.width_nm, color="grey", lw=0.8)
    ax.set_xlabel("barrier width d (nm)")
    ax.set_ylabel("tunneling probability P")
    ax.set_title(r"WKB: $P_D \approx P_H^{\sqrt{2}}$" + f"   (at d={truth.width_nm} nm, V={truth.barrier_ev} eV: ρ = {truth.rho:.1e})", fontsize=9)
    ax.legend(fontsize=7, ncol=3)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_tunneling.png", dpi=160)
    plt.close(fig)


def plot_odds(design, scenarios, rho):
    x = np.array(design.x_levels)
    j37 = design.temps_c.index(37.0)
    fig, axes = plt.subplots(1, len(scenarios), figsize=(9.5, 3.4), sharey=True)
    for ax, sc in zip(axes, scenarios):
        ts, tv = sc["ts"][:, j37].sum(1), sc["tv"][:, j37].sum(1)
        odds = ts / tv
        rel = odds / odds[0]
        err = rel * np.sqrt(1 / ts + 1 / tv + 1 / ts[0] + 1 / tv[0])
        ax.errorbar(x, rel, err, fmt="o", color="k", ms=4, capsize=2, label="simulated data")
        xx = np.linspace(0, 1, 50)
        f_hat = sc["per_T"][j37]["f"]
        ax.plot(xx, 1 - f_hat * xx * (1 - rho), "C0", label=f"fit: f = {f_hat:.3f}")
        ax.plot(xx, 1 - sc["true_f"] * xx * (1 - rho), "C3--", lw=1, label=f"truth: f = {sc['true_f']}")
        ax.axhline(1, color="grey", lw=0.6)
        ax.set_title(sc["name"], fontsize=9)
        ax.set_xlabel("D₂O fraction x")
        ax.legend(fontsize=7)
    axes[0].set_ylabel("ts:tv odds relative to H₂O")
    fig.tight_layout()
    fig.savefig(OUT / "fig2_odds_vs_d2o.png", dpi=160)
    plt.close(fig)


def plot_temperature(design, scenarios):
    temps = np.array(design.temps_c)
    fig, ax = plt.subplots(figsize=(6, 3.6))
    for k, sc in enumerate(scenarios):
        t = sc["temperature"]
        ax.errorbar(temps + 0.4 * (k - 1), t["f_T"], t["f_T_se"], fmt="o", color=f"C{k}", capsize=2, ms=4,
                    label=f"{sc['name']}: slope {1e3 * t['slope']:+.1f} ± {1e3 * t['slope_se']:.1f} ×10⁻³/K")
    tt = np.linspace(temps.min(), temps.max(), 50) + 273.15
    arr = np.exp(-Truth().ea_ev / KB_EV * (1 / tt - 1 / T_REF))
    ax.plot(tt - 273.15, 0.1 / (0.1 + 0.9 * arr), "k--", lw=1, label="tunneling prediction (F = 0.10)")
    ax.axhline(0, color="grey", lw=0.6)
    ax.set_xlabel("temperature (°C)")
    ax.set_ylabel("estimated quantum share f_T")
    ax.set_title("Temperature check: a real tunneling share falls as T rises", fontsize=9)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_temperature_check.png", dpi=160)
    plt.close(fig)


def plot_power(table, f_values, line_counts):
    fig, ax = plt.subplots(figsize=(5.5, 3.4))
    for f in f_values:
        ax.plot(line_counts, [table[(f, n)]["power"] for n in line_counts], "o-", label=f"true f_q = {f}")
    ax.axhline(0.8, color="grey", ls="--", lw=0.8)
    ax.axhline(0.05, color="grey", ls=":", lw=0.8)
    ax.set_xscale("log")
    ax.set_xticks(line_counts, [str(n) for n in line_counts])
    ax.minorticks_off()
    ax.set_xlabel(f"MA lines per condition ({len(Design().x_levels) * len(Design().temps_c)} conditions, {Design().generations} generations each)")
    ax.set_ylabel("power (one-sided, α = 0.05)")
    ax.set_ylim(0, 1.02)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT / "fig4_power.png", dpi=160)
    plt.close(fig)


# --- main ------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()

    truth, design = Truth(), Design()
    print(f"WKB: P_H = {wkb_probability(truth.barrier_ev, truth.width_nm, M_H):.2e}, "
          f"P_D = {wkb_probability(truth.barrier_ev, truth.width_nm, M_D):.2e}, rho = {truth.rho:.2e}")

    scenarios = [
        run_scenario("A: tunneling, f = 0.10", truth, design, seed=1),
        run_scenario("B: no tunneling, f = 0", replace(truth, f_q=0.0), design, seed=2),
        run_scenario("C: no tunneling + classical confound",
                     replace(truth, f_q=0.0, de_ts_extra_ev=0.004), design, seed=3),
    ]
    for sc in scenarios:
        per_t = ", ".join(f"{t:.0f}C: {r['f']:+.3f}±{r['se']:.3f}" for t, r in zip(design.temps_c, sc["per_T"]))
        t = sc["temperature"]
        print(f"{sc['name']:<40} f_hat = {sc['f_hat']:+.3f} ± {sc['se']:.3f} (z = {sc['z']:+.2f})  [{per_t}]\n"
              f"{'':<40} df/dT = {1e3 * t['slope']:+.1f} ± {1e3 * t['slope_se']:.1f} e-3/K "
              f"(tunneling predicts {1e3 * t['tunnel_pred_slope']:+.1f}; E_a from transversions = {t['ea_ev']:.2f} eV)")

    f_values, line_counts = (0.05, 0.10, 0.20, 0.0), (25, 50, 100, 200, 400)
    reps = 60 if args.quick else 300
    table = power_analysis(truth, design, f_values, line_counts, reps, seed=7)
    print(f"\nPower ({reps} simulated experiments per cell; f_q = 0 row is the false-positive rate):")
    print("lines/cond " + "".join(f"{n:>8}" for n in line_counts))
    for f in f_values:
        print(f"f_q = {f:<5}" + "".join(f"{table[(f, n)]['power']:>8.2f}" for n in line_counts))

    plot_physics(truth)
    plot_odds(design, scenarios, truth.rho)
    plot_temperature(design, scenarios)
    plot_power(table, [f for f in f_values if f > 0] + [0.0], line_counts)

    summary = {
        "truth": truth.__dict__ | {"rho": truth.rho},
        "design": design.__dict__,
        "scenarios": [{k: v for k, v in sc.items() if k not in ("ts", "tv")} for sc in scenarios],
        "power": {f"f={f},lines={n}": v for (f, n), v in table.items()},
        "power_reps": reps,
    }
    (OUT / "results.json").write_text(json.dumps(summary, indent=2, default=float))
    print("\nwrote figures and results.json to", OUT)


if __name__ == "__main__":
    main()
