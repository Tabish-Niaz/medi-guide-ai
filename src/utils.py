import json
import re

def parse_json_safely(text):
    try:
        # LLM kabhi kabhi json aur  text ke sath bhejta hai, usay remove karna
        clean_text = re.sub(r'json\n|\n|```', '', text).strip()
        return json.loads(clean_text)
    except Exception as e:
        return None