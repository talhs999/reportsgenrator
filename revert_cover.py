import re

with open('report/templates/report.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Revert Cover CSS
start_idx = text.find('.cover-page {')
end_idx = text.find('.cover-title {', start_idx)

if start_idx != -1 and end_idx != -1:
    new_css = '''
.cover-page {
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    position: relative;
    overflow: hidden;
    background: var(--white);
}

.cover-bg {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 55%;
    background: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary) 60%, #000000));
}

.cover-bg::after {
    content: "";
    position: absolute;
    bottom: -60px;
    left: 0;
    right: 0;
    height: 120px;
    background: var(--white);
    transform: skewY(-3deg);
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
    height: 48px;
    width: auto;
}
'''
    text = text[:start_idx] + new_css.strip() + '\n\n' + text[end_idx:]
    print('Reverted cover CSS successfully')
else:
    print('Failed to find cover CSS')

# Change h1 text color back to primary if logo is absent
text = text.replace('color: var(--white); font-size: 24pt;', 'color: var(--primary); font-size: 24pt;')

# 2. Fix logo on last page
disclaimer_idx = text.find('<!-- Disclaimer -->')
if disclaimer_idx != -1:
    end_part = text[disclaimer_idx:]
    end_part = end_part.replace('{% if header_logo_uri %}', '{% if cover_logo_uri %}')
    end_part = end_part.replace('src="{{ header_logo_uri }}"', 'src="{{ cover_logo_uri }}"')
    text = text[:disclaimer_idx] + end_part
    print('Replaced logo on last page')

with open('report/templates/report.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
