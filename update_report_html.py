import re

with open('report/templates/report.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace inner page header logos (which use logo_data_uri) with header_logo_uri
text = text.replace('{% if logo_data_uri %}', '{% if header_logo_uri %}')
text = text.replace('src="{{ logo_data_uri }}"', 'src="{{ header_logo_uri }}"')

# For the cover page, let's just make sure it uses cover_logo_uri
cover_html_idx = text.find('<div class="cover-logo-row">')

if cover_html_idx != -1:
    end_row = text.find('</div>', text.find('</div>', cover_html_idx) + 6) + 6
    old_row = text[cover_html_idx:end_row]
    new_row = '''<div class="cover-logo-row">
        <div class="cover-logo-container">
            {% if cover_logo_uri %}
            <img src="{{ cover_logo_uri }}" class="cover-logo" alt="Logo">
            {% else %}
            <h1 style="color: var(--white); font-size: 24pt;">{{ company_name }}</h1>
            {% endif %}
        </div>
        <div class="cover-reg-badge">{{ registration }}</div>
    </div>'''
    text = text.replace(old_row, new_row)
else:
    print('Could not find cover logo row HTML')

with open('report/templates/report.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated logo variables successfully')
