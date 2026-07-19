import re

with open('report/templates/report.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS
css_old = """.cover-title {
    font-size: 32pt;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin-bottom: 8px;
}

.cover-subtitle {
    font-size: 12pt;
    font-weight: 400;
    opacity: 0.85;
    letter-spacing: 0.5px;
}"""

css_new = """.package-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 10pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
    color: var(--white);
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.4);
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.cover-title {
    font-size: 32pt;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin-bottom: 8px;
    color: var(--white);
}

.cover-subtitle {
    font-size: 12pt;
    font-weight: 400;
    opacity: 0.85;
    letter-spacing: 0.5px;
    color: var(--white);
}"""

text = text.replace(css_old, css_new)

# 2. Update HTML
html_old = """        <div>
            <div class="cover-title">Vehicle History Report</div>
            <div class="cover-subtitle">Comprehensive {{ package | title }} Assessment</div>
        </div>"""

html_new = """        <div>
            <div class="package-badge">{{ package | upper }} REPORT</div>
            <div class="cover-title">Vehicle History Report</div>
            <div class="cover-subtitle">Comprehensive {{ package | title }} Assessment</div>
        </div>"""

text = text.replace(html_old, html_new)

with open('report/templates/report.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated cover page CSS and HTML successfully!')
