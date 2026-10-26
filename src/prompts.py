# from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# # Exact JSON structure required by assignment
# JSON_SCHEMA = """
# {
#   "summary": "Patient symptom summary",
#   "possible_conditions": [ {"name": "Condition 1", "reason": "Reason 1"} ],
#   "urgency_level": "LOW, MEDIUM, HIGH, or EMERGENCY",
#   "recommended_next_steps": ["Step 1", "Step 2"],
#   "questions_for_doctor": ["Question 1", "Question 2"],
#   "warning_signs": ["Sign 1", "Sign 2"]
# }
# """

# SYSTEM_PROMPT = """You are MediGuide AI, an educational medical AI assistant.
# IMPORTANT SAFETY RULES:
# 1. You are NOT a doctor. NEVER provide a confirmed diagnosis.
# 2. If symptoms are severe, set urgency_level to "EMERGENCY".
# 3. Your output MUST be ONLY valid JSON matching this exact schema:
# """ + JSON_SCHEMA + """
# 4. Always respond in this language: {language}
# """

# chat_prompt = ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
#     HumanMessagePromptTemplate.from_template(
#         "Age: {age}\nGender: {gender}\nSymptoms: {symptoms}\nDuration: {duration}\nSeverity (1-10): {severity}\nConditions: {conditions}\nMedications: {medications}\nNotes: {notes}"
#     )
# ])

# # For streaming narrative
# NARRATIVE_PROMPT = """You are an educational medical AI. Based on the patient details, write a short, empathetic paragraph summarizing their situation. End with a strong medical disclaimer. DO NOT diagnose. Respond in: {language}"""

# narrative_chat_prompt = ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(NARRATIVE_PROMPT),
#     HumanMessagePromptTemplate.from_template("Symptoms: {symptoms}, Severity: {severity}, Duration: {duration}")
# ])


from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# JSON Schema ke braces {} ko double {{ }} kar diya gaya hai
JSON_SCHEMA = """
{{
  "summary": "Patient symptom summary",
  "possible_conditions": [ {{"name": "Condition 1", "reason": "Reason 1"}} ],
  "urgency_level": "LOW, MEDIUM, HIGH, or EMERGENCY",
  "recommended_next_steps": ["Step 1", "Step 2"],
  "questions_for_doctor": ["Question 1", "Question 2"],
  "warning_signs": ["Sign 1", "Sign 2"]
}}
"""

SYSTEM_PROMPT = """You are MediGuide AI, an educational medical AI assistant.
IMPORTANT SAFETY RULES:
1. You are NOT a doctor. NEVER provide a confirmed diagnosis.
2. If symptoms are severe, set urgency_level to "EMERGENCY".
3. Your output MUST be ONLY valid JSON matching this exact schema:
""" + JSON_SCHEMA + """
4. Always respond in this language: {language}
"""

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
    HumanMessagePromptTemplate.from_template(
        "Age: {age}\nGender: {gender}\nSymptoms: {symptoms}\nDuration: {duration}\nSeverity (1-10): {severity}\nConditions: {conditions}\nMedications: {medications}\nNotes: {notes}"
    )
])

# For streaming narrative
NARRATIVE_PROMPT = """You are an educational medical AI. Based on the patient details, write a short, empathetic paragraph summarizing their situation. End with a strong medical disclaimer. DO NOT diagnose. Respond in: {language}"""

narrative_chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(NARRATIVE_PROMPT),
    HumanMessagePromptTemplate.from_template("Symptoms: {symptoms}, Severity: {severity}, Duration: {duration}")
])