import re

with open('report/templates/report.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_cover_css = '''
.cover-page {
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    position: relative;
    overflow: hidden;
    background: var(--ink);
}

.cover-bg {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 100%;
    background-image: url("{{ cover_bg_uri }}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.8;
}

.cover-bg::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(0,0,0,0.6), rgba(0,0,0,0.9));
}

.cover-content {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 30mm 25mm;
}

.cover-logo-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25mm;
}

.cover-logo {
    height: 60px;
    width: auto;
}
'''

start_idx = text.find('.cover-page {')
end_idx = text.find('.cover-title {', start_idx)

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + new_cover_css.strip() + '\n\n' + text[end_idx:]
    
    # Also need to replace logo_data_uri with cover_logo_uri and header_logo_uri
    text = text.replace('{% if logo_data_uri %}', '{% if cover_logo_uri %}')
    text = text.replace('src="{{ logo_data_uri }}"', 'src="{{ cover_logo_uri }}"')
    text = text.replace('src="{{ header_logo_uri }}"', 'src="{{ cover_logo_uri }}"') # wait
    
    # Let's just fix the logo variables manually
    with open('report/templates/report.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Replaced cover CSS successfully')
else:
    print('Failed to find cover CSS')
