import re

with open('api/scraper_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the panel processing block around line 313
old_block = """                # Tax/MOT from panels
                for k, v in dvla_data.items():
                    vl = v.lower() if isinstance(v, str) else ""
                    if "_panel" in k:
                        if "tax" in vl:
                            if "taxed" in vl:
                                result["tax_status"] = "Taxed"
                            elif "sorn" in vl:
                                result["tax_status"] = "SORN"
                            elif "not taxed" in vl or "untaxed" in vl:
                                result["tax_status"] = "Not Taxed"
                        if "mot" in vl:
                            if "valid mot" in vl:
                                result["mot_status"] = "Valid"
                            elif "no mot" in vl or "expired" in vl:
                                result["mot_status"] = "Expired / No MOT\"\"\""""

# The exact old block might differ slightly. Let's just find it using regex or replace it directly.
