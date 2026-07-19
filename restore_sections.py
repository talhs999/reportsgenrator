import re

with open('report/generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('stolen_check = None', 'stolen_check = templated.get_stolen_check(registration)')
text = text.replace('finance_check = None', 'finance_check = templated.get_finance_check(registration)')
text = text.replace('writeoff_check = None', 'writeoff_check = templated.get_writeoff_check(registration)')

text = text.replace('def _calculate_pages(package: str, tests_count: int, has_additional_info: bool, has_insurance: bool) -> dict:',
                    'def _calculate_pages(package: str, tests_count: int, has_additional_info: bool, has_insurance: bool, has_theft: bool = True, has_finance: bool = True, has_writeoff: bool = True) -> dict:')

# We also need to add them back to _calculate_pages body
def_body = text.split('def _calculate_pages')[1]
def_body = def_body.replace("    p['theft'] = None", """    if has_theft:
        p['theft'] = current
        current += 1
    else:
        p['theft'] = None""")

def_body = def_body.replace("    p['finance'] = None", """    if has_finance:
        p['finance'] = current
        current += 1
    else:
        p['finance'] = None""")

def_body = def_body.replace("    p['writeoff'] = None", """    if has_writeoff:
        p['writeoff'] = current
        current += 1
    else:
        p['writeoff'] = None""")

text = text.split('def _calculate_pages')[0] + 'def _calculate_pages' + def_body

# Update context
text = text.replace('"theft": None,', '"theft": stolen_check,')
text = text.replace('"finance": None,', '"finance": finance_check,')
text = text.replace('"writeoff": None,', '"writeoff": writeoff_check,')

# Update calculate_pages call
text = text.replace('p = _calculate_pages(package, tests_count, has_additional_info, has_insurance)',
                    'p = _calculate_pages(package, tests_count, has_additional_info, has_insurance, True, True, True)')

with open('report/generator.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('Restored sections successfully')
