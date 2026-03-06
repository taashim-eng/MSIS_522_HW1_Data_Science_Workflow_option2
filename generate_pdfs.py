"""
Generate PDF infographics (dark + light beige) using Playwright.
Ensures all content fits on A4 landscape pages with no cut-offs.
"""
import asyncio, os, shutil
from pathlib import Path
from playwright.async_api import async_playwright

REPO = Path(r"C:\Users\taash\antigravitygithub\Taashi_Github\MSIS_522_HW1_Data_Science_Workflow_option2")
ONEDRIVE = Path(r"C:\Users\taash\OneDrive\UW\Class\Winter 2025-2026\MSIS 522 B Advanced Machine Learning\Homework 1 The Complete Data Science Workflow\Option 2 for the credit scoring")

HTML_SRC = REPO / "infographic.html"

# CSS override block injected just before </style> to force light theme
BEIGE_OVERRIDE_CSS = """
/* ═══════════════════ LIGHT BEIGE OVERRIDE ═══════════════════ */
:root {
  --navy:     #FAF6F1 !important;
  --dark:     #F5EFE6 !important;
  --white:    #1C1108 !important;
  --off-white:#2D1B06 !important;
  --slate:    #4A3828 !important;
  --card-bg:  rgba(120,80,30,0.05) !important;
  --card-br:  rgba(120,80,30,0.12) !important;
  --accent-gradient: linear-gradient(135deg, #1E50B0, #057A8C) !important;
  --warm-gradient:   linear-gradient(135deg, #C47506, #C05010) !important;
  --success-gradient:linear-gradient(135deg, #15803D, #0D7A6A) !important;
}
html, body { background: #F5EFE6 !important; }
.page {
  background: #FAF6F1 !important;
  color: #1C1108 !important;
  box-shadow: 0 4px 24px rgba(120,80,30,0.10) !important;
}
.page::before {
  background: radial-gradient(ellipse at 20% 20%, rgba(160,120,50,0.05) 0%, transparent 60%),
              radial-gradient(ellipse at 80% 80%, rgba(140,100,40,0.04) 0%, transparent 60%) !important;
}

/* Typography */
.page-title { background: linear-gradient(135deg, #1E50B0, #057A8C) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; background-clip: text !important; }
.page-subtitle { color: #5C4A3A !important; }
.section-title { color: #0891B2 !important; border-bottom-color: rgba(8,145,178,0.25) !important; }
.subsection-title { color: #1C1108 !important; }
.body-text { color: #5D4E3F !important; }
.body-text strong { color: #1C1108 !important; }
.small-text { color: #6B5C4E !important; }
.small-text strong { color: #1C1108 !important; }

/* Cards */
.card { background: rgba(120,80,30,0.04) !important; border-color: rgba(120,80,30,0.12) !important; }

/* Icon circles */
.icon-blue   { background: rgba(37,99,235,0.10) !important; color: #2563EB !important; }
.icon-cyan   { background: rgba(6,182,212,0.10) !important; color: #0891B2 !important; }
.icon-green  { background: rgba(22,163,74,0.10) !important; color: #16A34A !important; }
.icon-amber  { background: rgba(217,119,6,0.10) !important; color: #D97706 !important; }
.icon-purple { background: rgba(124,58,237,0.10) !important; color: #7C3AED !important; }
.icon-red    { background: rgba(220,38,38,0.10) !important; color: #DC2626 !important; }
.icon-pink   { background: rgba(219,39,119,0.10) !important; color: #DB2777 !important; }
.icon-teal   { background: rgba(13,148,136,0.10) !important; color: #0D9488 !important; }

/* Tables */
.info-table th { background: rgba(8,145,178,0.08) !important; color: #0891B2 !important; border-bottom-color: rgba(8,145,178,0.20) !important; }
.info-table td { color: #5D4E3F !important; border-bottom-color: rgba(120,80,30,0.06) !important; }
.info-table td strong { color: #1C1108 !important; }

/* Badges */
.badge-blue   { background: rgba(37,99,235,0.10) !important; color: #2563EB !important; }
.badge-green  { background: rgba(22,163,74,0.12) !important; color: #16A34A !important; }
.badge-amber  { background: rgba(217,119,6,0.12) !important; color: #D97706 !important; }
.badge-red    { background: rgba(220,38,38,0.12) !important; color: #DC2626 !important; }
.badge-purple { background: rgba(124,58,237,0.10) !important; color: #7C3AED !important; }
.badge-cyan   { background: rgba(8,145,178,0.10) !important; color: #0891B2 !important; }

/* Stat callouts — keep gradients but darker */
.stat-big { background: linear-gradient(135deg, #1E50B0, #057A8C) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; background-clip: text !important; }
.stat-big-amber { background: linear-gradient(135deg, #C47506, #C05010) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; background-clip: text !important; }
.stat-big-green { background: linear-gradient(135deg, #15803D, #0D7A6A) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; background-clip: text !important; }
.stat-label { color: #7A6B5C !important; }

/* Metric cards */
.metric-card { background: rgba(120,80,30,0.04) !important; border-color: rgba(120,80,30,0.12) !important; }

/* Highlight box */
.highlight-box { background: linear-gradient(135deg, rgba(30,80,176,0.06), rgba(5,122,140,0.05)) !important; border-color: rgba(30,80,176,0.15) !important; }

/* Dividers */
.divider { background: rgba(120,80,30,0.10) !important; }

/* Progress bars */
.progress-bar { background: rgba(120,80,30,0.08) !important; }

/* Flow arrow */
.flow-arrow { color: #0891B2 !important; }

/* Step number */
.step-number { background: linear-gradient(135deg, #1E50B0, #057A8C) !important; color: white !important; }

/* Footer */
.page-footer { color: #8A7B6C !important; border-top-color: rgba(120,80,30,0.10) !important; }

/* Page numbers */
.page [style*="color:rgba(37,99,235,0.3)"] { color: rgba(160,120,50,0.25) !important; }

/* Inline styles — catch remaining white text in styled elements */
[style*="color:var(--white)"] { color: #1C1108 !important; }
[style*="color:#64748B"] { color: #7A6B5C !important; }
[style*="color:var(--amber)"] { color: #D97706 !important; }
[style*="color:var(--cyan)"] { color: #0891B2 !important; }
[style*="color:var(--green)"] { color: #16A34A !important; }
[style*="color:var(--purple)"] { color: #7C3AED !important; }
[style*="color:var(--blue-lt)"] { color: #2563EB !important; }
[style*="color: #CBD5E1"] { color: #4A3828 !important; }

/* Card accent borders keep their colors */
.card-accent { border-left-color: var(--blue) !important; }
.card-red { border-left-color: var(--red) !important; }
.card-cyan { border-left-color: var(--cyan) !important; }
.card-green { border-left-color: var(--green) !important; }
.card-amber { border-left-color: var(--amber) !important; }
.card-purple { border-left-color: var(--purple) !important; }

/* Ensure model cards text is dark */
.grid-5 .card div[style*="font-weight:700"] { color: #1C1108 !important; }
"""


def create_beige_html(src_html: str) -> str:
    """Inject beige override CSS into the HTML."""
    return src_html.replace(
        "</style>",
        BEIGE_OVERRIDE_CSS + "\n</style>"
    ).replace(
        "<title>Alternative Credit Scoring — Project Infographic</title>",
        "<title>Alternative Credit Scoring — Project Infographic (Light Beige)</title>"
    )


async def render_pdf(html_path: str, pdf_path: str):
    """Render an HTML file to a multi-page A4 landscape PDF."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
        await page.wait_for_timeout(2500)
        await page.pdf(
            path=pdf_path,
            format="A4",
            landscape=True,
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()
        print(f"PDF saved: {pdf_path}")


async def main():
    src_html = HTML_SRC.read_text(encoding="utf-8")

    # ── 1. Dark version PDF ──
    dark_pdf = str(REPO / "infographic_dark.pdf")
    await render_pdf(str(HTML_SRC), dark_pdf)
    shutil.copy2(dark_pdf, str(ONEDRIVE / "infographic_dark.pdf"))
    print("Copied dark PDF to OneDrive")

    # ── 2. Light beige version ──
    beige_html = create_beige_html(src_html)
    beige_html_path = str(REPO / "infographic_light.html")
    Path(beige_html_path).write_text(beige_html, encoding="utf-8")
    print(f"Beige HTML saved: {beige_html_path}")

    beige_pdf = str(REPO / "infographic_light.pdf")
    await render_pdf(beige_html_path, beige_pdf)
    shutil.copy2(beige_pdf, str(ONEDRIVE / "infographic_light.pdf"))
    print("Copied light PDF to OneDrive")

    print("\nDone! Both PDFs generated.")


if __name__ == "__main__":
    asyncio.run(main())
