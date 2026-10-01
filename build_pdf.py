"""Build a paper PDF from a Markdown source using headless Chrome.

Usage: python build_pdf.py [source.md] [output.pdf]
The source starts with a front-matter block (title, author, date, keywords,
abstract) between --- lines. Math in $...$ or $$...$$ is rendered with KaTeX.
"""
import html, pathlib, re, shutil, subprocess, sys, time, markdown

HERE = pathlib.Path(__file__).parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "toe-merged.md"
PDF = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "UTOE-Universal-Theory-of-Everything.pdf"
HTML = HERE / "paper.html"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

text = SRC.read_text(encoding="utf-8")
_, front, md = text.split("---\n", 2)
meta = dict(line.split(": ", 1) for line in front.strip().splitlines())

# Keep math away from the Markdown parser, then put it back verbatim.
stash = []
def protect(s):
    def keep(m):
        stash.append(html.escape(m.group(0), quote=False))
        return f"MATHPH{len(stash) - 1}END"
    return re.sub(r"\$\$.+?\$\$|\$[^$\n]+?\$", keep, s, flags=re.S)
def restore(s):
    return re.sub(r"MATHPH(\d+)END", lambda m: stash[int(m.group(1))], s)

md = re.sub(r"^## References\s*$", "## References {.nonum}", md, flags=re.M)
body = restore(markdown.markdown(protect(md), extensions=["tables", "attr_list"]))
abstract = restore(markdown.markdown(protect(meta["abstract"])))[3:-4]  # strip <p>

KATEX = ".katex"  # local copy of KaTeX 0.16.11 dist, so builds work offline
page = f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html.escape(meta['title'])}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css">
<script defer src="{KATEX}/katex.min.js"></script>
<script defer src="{KATEX}/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{delimiters: [
    {{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}})"></script>
<style>
@page {{ size: A4; margin: 22mm 20mm 22mm 20mm;
  @bottom-center {{ content: counter(page); font: 9pt 'Times New Roman'; }} }}
body {{ font: 11pt/1.5 'Times New Roman', Georgia, serif; color: #111; counter-reset: h2; }}
.title {{ text-align: center; margin-bottom: 18pt; }}
.title h1 {{ font-size: 19pt; line-height: 1.25; margin: 0 0 10pt; }}
.title .author {{ font-size: 12pt; }}
.title .date {{ font-size: 10pt; color: #444; margin-top: 4pt; }}
.abstract {{ margin: 0 10mm 14pt; font-size: 10pt; text-align: justify; }}
.abstract b {{ display: block; text-align: center; margin-bottom: 4pt; font-size: 10.5pt; }}
.keywords {{ margin: 0 10mm 18pt; font-size: 9.5pt; }}
p, li {{ text-align: justify; }}
h2 {{ font-size: 13pt; margin: 18pt 0 6pt; counter-reset: h3; break-after: avoid; }}
h2:not(.nonum)::before {{ counter-increment: h2; content: counter(h2) ". "; }}
h3 {{ font-size: 11.5pt; font-style: italic; margin: 12pt 0 4pt; break-after: avoid; }}
h3::before {{ counter-increment: h3; content: counter(h2) "." counter(h3) " "; }}
table {{ border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 8pt 0; }}
tr {{ break-inside: avoid; }}
th, td {{ border-top: 1px solid #999; border-bottom: 1px solid #999; padding: 4pt 6pt; text-align: left; vertical-align: top; }}
th {{ border-top: 1.5px solid #000; border-bottom: 1px solid #000; }}
blockquote {{ margin: 8pt 12mm; font-style: italic; }}
img {{ display: block; max-width: 85%; margin: 8pt auto; break-inside: avoid; }}
pre {{ font-size: 9pt; background: #f4f4f4; padding: 6pt 8pt; }}
blockquote p {{ text-align: left; }}
.katex-display {{ margin: 8pt 0; }}
tr {{ break-inside: avoid; }}
.katex {{ font-size: 1.05em; }}
h2.nonum + ol {{ font-size: 9.5pt; padding-left: 20pt; }}
h2.nonum + ol li {{ margin-bottom: 3pt; text-align: left; }}
</style></head><body>
<div class="title">
  <h1>{html.escape(meta['title'])}</h1>
  <div class="author">{html.escape(meta['author'])}</div>
  <div class="date">{html.escape(meta['date'])}</div>
</div>
<div class="abstract"><b>Abstract</b>{abstract}</div>
<div class="keywords"><b>Keywords:</b> {html.escape(meta['keywords'])}</div>
{body}
</body></html>"""

HTML.write_text(page, encoding="utf-8")
PDF.unlink(missing_ok=True)
proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                         f"--user-data-dir={HERE / '.chrome-build'}", f"--print-to-pdf={PDF}", HTML.as_uri()])
# Headless Chrome sometimes writes the PDF and then never exits, so wait for the
# file to appear and stop changing rather than for the process.
for _ in range(120):
    time.sleep(1)
    if proc.poll() is not None or (PDF.exists() and PDF.stat().st_size and time.time() - PDF.stat().st_mtime > 3):
        break
subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)
shutil.rmtree(HERE / ".chrome-build", ignore_errors=True)
if not PDF.exists():
    sys.exit("PDF was not produced")
print("wrote", PDF)
