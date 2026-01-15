#!/usr/bin/env python3
"""
Convert markdown files to PDF using markdown2 and weasyprint
Install: pip install markdown2 weasyprint
"""

import markdown2
from weasyprint import HTML
from pathlib import Path

def convert_md_to_pdf(md_file, pdf_file=None):
    """Convert markdown file to PDF"""
    md_path = Path(md_file)
    
    if pdf_file is None:
        pdf_file = md_path.with_suffix('.pdf')
    
    # Read markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML
    html_content = markdown2.markdown(md_content, extras=['tables', 'fenced-code-blocks'])
    
    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 40px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 8px;
                margin-top: 30px;
            }}
            h3 {{
                color: #7f8c8d;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                font-size: 9pt;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            hr {{
                border: none;
                border-top: 2px solid #ecf0f1;
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert to PDF
    HTML(string=styled_html).write_pdf(pdf_file)
    print(f"✅ PDF created: {pdf_file}")

if __name__ == "__main__":
    # Convert feature_comparison.md
    convert_md_to_pdf("docs/feature_comparison.md")
    print("Conversion complete!")
