import markdown

base = r'C:\Users\taash\OneDrive\UW\Class\Winter 2025-2026\MSIS 522 B Advanced Machine Learning\Homework 1 The Complete Data Science Workflow\Option 2 for the credit scoring'

with open(base + r'\research_writeup.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

css = """
body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #333; }
h1 { color: #1a1a1a; border-bottom: 3px solid #2196F3; padding-bottom: 10px; }
h2 { color: #1565C0; margin-top: 30px; }
h3 { color: #1976D2; }
table { border-collapse: collapse; width: 100%; margin: 15px 0; }
th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
th { background-color: #2196F3; color: white; }
tr:nth-child(even) { background-color: #f9f9f9; }
code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
pre { background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }
hr { border: none; border-top: 2px solid #e0e0e0; margin: 30px 0; }
"""

full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Alternative Credit Scoring - Dataset Research</title><style>{css}</style></head><body>{html_body}</body></html>"

with open(base + r'\research_writeup.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('HTML generated: research_writeup.html')
