import re

with open('report/templates/report.html', 'r', encoding='utf-8') as f:
    text = f.read()

def wrap_section(html, keyword, var_name):
    # Find the comment block that starts the section
    start_str = f"NEW PAGE: {keyword.upper()}"
    idx = html.find(start_str)
    if idx == -1: return html
    
    # Go back to <!-- ════════════
    block_start = html.rfind("<!-- ════════════", 0, idx)
    
    # Go forward to find the matching </div> for <div class="page">
    page_div_idx = html.find('<div class="page">', block_start)
    if page_div_idx == -1: return html
    
    # Now find the end of this div
    count = 0
    end_idx = -1
    pos = page_div_idx
    while pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        
        if next_open != -1 and next_open < next_close:
            count += 1
            pos = next_open + 4
        elif next_close != -1:
            count -= 1
            pos = next_close + 6
            if count == 0:
                end_idx = pos
                break
        else:
            break
            
    if end_idx != -1:
        # Wrap it!
        wrapped = f"{{% if {var_name} %}}\n" + html[block_start:end_idx] + f"\n{{% endif %}}"
        html = html[:block_start] + wrapped + html[end_idx:]
    
    return html

text = wrap_section(text, "Insurance Verification", "insurance")

with open('report/templates/report.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Wrapped insurance successfully!")
