# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")


# # DISCLAIMER
# DISCLAIMER = "⚠️ *IMPORTANT MEDICAL NOTICE:* This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# # Sidebar
# with st.sidebar:
#     st.title("🩺 MediGuide AI")
#     st.caption("AI-Powered Medical Symptom Assessment")
#     st.error(DISCLAIMER)
    
#     st.subheader("Settings")
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"])
#     enable_caching(cache_option)
    
#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"])

# # Main Area
# st.title("Patient Symptom Assessment")
# st.warning(DISCLAIMER)

# # Form Inputs
# with st.form("patient_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Sore Throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 5)
    
#     conditions = st.text_area("Existing Medical Conditions (Optional)")
#     medications = st.text_area("Current Medications (Optional)")
#     notes = st.text_area("Additional Notes (Optional)")
    
#     submitted = st.form_submit_button("Analyse Symptoms", type="primary")

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()
        
#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()
        
#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms, 
#         "duration": duration, "severity": severity, 
#         "conditions": conditions, "medications": medications, 
#         "notes": notes, "language": language
#     }
    
#     st.divider()
#     st.subheader("🤖 Assessment Dashboard")
    
#     # Streaming Narrative Section
#     st.markdown("### AI Narrative Analysis")
#     with st.chat_message("assistant"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
    
#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)
        
#         if result:
#             # Urgency Level Logic
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.error(f"🚨 URGENCY LEVEL: {urgency} - SEEK IMMEDIATE MEDICAL HELP!")
#             elif "MEDIUM" in urgency:
#                 st.warning(f"⚠️ URGENCY LEVEL: {urgency} - Please consult a doctor soon.")
#             else:
#                 st.success(f"🟢 URGENCY LEVEL: {urgency} - Monitor symptoms.")
            
#             col_a, col_b = st.columns(2)
            
#             with col_a:
#                 st.info(f"*Summary:* {result.get('summary', '')}")
                
#                 st.markdown("### Possible Conditions (Educational Only)")
#                 for cond in result.get("possible_conditions", []):
#                     st.write(f"- *{cond.get('name')}*: {cond.get('reason')}")
                    
#             with col_b:
#                 st.markdown("### Recommended Next Steps")
#                 for step in result.get("recommended_next_steps", []):
#                     st.write(f"- {step}")
                    
#                 st.markdown("### Warning Signs (Seek Help if seen)")
#                 for sign in result.get("warning_signs", []):
#                     st.write(f"🛑 {sign}")
            
#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)


# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")

# # ==========================================
# # ADVANCED CUSTOM CSS FOR PREMIUM GLASSMORPHIC UI
# # ==========================================
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
#     html, body, [class*="css"] { 
#         font-family: 'Plus Jakarta Sans', sans-serif !important; 
#         color: #e2e8f0 !important; 
#     }
    
#     /* Main Background */
#     [data-testid="stAppViewContainer"] {
#         background-color: #0b0c10 !important;
#         background-image: 
#             radial-gradient(circle at top right, rgba(79, 70, 229, 0.08), transparent 40%), 
#             radial-gradient(circle at bottom left, rgba(147, 51, 234, 0.05), transparent 40%) !important;
#     }
    
#     /* Top Header */
#     [data-testid="stHeader"] {
#         background-color: transparent !important;
#     }
    
#     /* Sidebar */
#     [data-testid="stSidebar"] {
#         background-color: #08090d !important;
#         border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
#     }
    
#     /* Buttons */
#     div.stButton > button {
#         background: linear-gradient(135deg, #3b82f6, #a855f7) !important;
#         color: #ffffff !important;
#         font-weight: 600 !important;
#         border: none !important;
#         border-radius: 10px !important;
#         box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
#         transition: all 0.3s ease !important;
#     }
#     div.stButton > button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5) !important;
#     }
    
#     /* Input Fields */
#     .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
#         background-color: #0f111a !important;
#         border: 1px solid rgba(255, 255, 255, 0.08) !important;
#         border-radius: 8px !important;
#         color: #e2e8f0 !important;
#     }
    
#     /* Form Container Glass Effect */
#     [data-testid="stForm"] {
#         background-color: rgba(255, 255, 255, 0.02) !important;
#         border: 1px solid rgba(255, 255, 255, 0.05) !important;
#         border-radius: 12px !important;
#         padding: 20px !important;
#     }
    
#     /* Dropdown Menus */
#     div[role="listbox"] {
#         background-color: #0F172A !important;
#         border: 1px solid rgba(255, 255, 255, 0.08) !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # DISCLAIMER
# DISCLAIMER = "⚠️ **IMPORTANT MEDICAL NOTICE:** This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# # Sidebar
# with st.sidebar:
#     st.markdown("""
#     <div style="background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(139, 92, 246, 0.1)); padding: 16px; border-radius: 14px; margin-bottom: 20px; border: 1px solid rgba(99, 102, 241, 0.15);">
#         <h2 style="margin:0; font-size: 1.4rem; font-weight: 800; background: -webkit-linear-gradient(45deg, #3b82f6, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🩺 MediGuide AI</h2>
#         <p style="margin:0; font-size: 0.8rem; color: #94a3b8;">AI Symptom Assessment</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.error(DISCLAIMER)
    
#     st.markdown("<p style='font-size: 0.72rem; font-weight: 700; color: #475569; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 24px;'>Settings</p>", unsafe_allow_html=True)
    
#     # SQLite set as default (index=2)
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2)
#     enable_caching(cache_option)
    
#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"])

# # Main Area
# st.markdown("<h1 style='font-weight: 800; letter-spacing: -1px; margin-bottom: 5px;'>Patient Symptom Assessment</h1>", unsafe_allow_html=True)
# st.warning(DISCLAIMER)

# # Form Inputs
# with st.form("patient_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Sore Throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 5)
    
#     conditions = st.text_area("Existing Medical Conditions (Optional)")
#     medications = st.text_area("Current Medications (Optional)")
#     notes = st.text_area("Additional Notes (Optional)")
    
#     submitted = st.form_submit_button("✨ Analyse Symptoms", use_container_width=True)

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()
        
#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()
        
#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms, 
#         "duration": duration, "severity": severity, 
#         "conditions": conditions, "medications": medications, 
#         "notes": notes, "language": language
#     }
    
#     st.divider()
#     st.markdown("<h2 style='font-weight: 700; color: #a855f7;'>🤖 Assessment Dashboard</h2>", unsafe_allow_html=True)
    
#     # Streaming Narrative Section
#     st.markdown("### AI Narrative Analysis")
#     with st.chat_message("assistant", avatar="✨"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
    
#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)
        
#         if result:
#             # Urgency Level Logic - Syntax Fixed
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.error(f"🚨 **URGENCY LEVEL: {urgency}** - SEEK IMMEDIATE MEDICAL HELP!")
#             elif "MEDIUM" in urgency:
#                 st.warning(f"⚠️ **URGENCY LEVEL: {urgency}** - Please consult a doctor soon.")
#             else:
#                 st.success(f"🟢 **URGENCY LEVEL: {urgency}** - Monitor symptoms.")
            
#             col_a, col_b = st.columns(2)
            
#             with col_a:
#                 st.info(f"**Summary:** {result.get('summary', '')}")
                
#                 st.markdown("### Possible Conditions (Educational Only)")
#                 for cond in result.get("possible_conditions", []):
#                     st.write(f"- **{cond.get('name')}**: {cond.get('reason')}")
                    
#             with col_b:
#                 st.markdown("### Recommended Next Steps")
#                 for step in result.get("recommended_next_steps", []):
#                     st.write(f"- {step}")
                    
#                 st.markdown("### Warning Signs (Seek Help if seen)")
#                 for sign in result.get("warning_signs", []):
#                     st.write(f"🛑 {sign}")
            
#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)



# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")

# # ==========================================
# # PDF RAG AGENT STYLE - PREMIUM UI CSS
# # ==========================================
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
#     html, body, [class*="css"] { 
#         font-family: 'Plus Jakarta Sans', sans-serif !important; 
#         background-color: #0b0c10 !important; 
#         color: #e2e8f0 !important; 
#     }
    
#     /* Main Background like PDF RAG Agent */
#     .stApp, [data-testid="stAppViewContainer"] { 
#         background: radial-gradient(circle at top right, rgba(79, 70, 229, 0.08), transparent), 
#                     radial-gradient(circle at bottom left, rgba(147, 51, 234, 0.05), transparent), 
#                     #0c0d14 !important; 
#     }
    
#     [data-testid="stHeader"] {
#         background-color: transparent !important;
#     }
    
#     [data-testid="stSidebar"] { 
#         background-color: #08090d !important; 
#         border-right: 1px solid rgba(255, 255, 255, 0.04) !important; 
#         padding-top: 10px; 
#     }
    
#     /* Brand Logo Container from RAG Agent */
#     .brand-container { 
#         background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(139, 92, 246, 0.1)); 
#         padding: 16px; 
#         border-radius: 14px; 
#         margin-bottom: 20px; 
#         display: flex; 
#         align-items: center; 
#         gap: 12px; 
#         border: 1px solid rgba(99, 102, 241, 0.15); 
#     }
#     .brand-logo { 
#         background: linear-gradient(135deg, #2563eb, #8b5cf6); 
#         border-radius: 10px; 
#         width: 38px; 
#         height: 38px; 
#         display: flex; 
#         align-items: center; 
#         justify-content: center; 
#         box-shadow: 0px 4px 12px rgba(37, 99, 235, 0.3); 
#         font-size: 20px;
#     }
#     .brand-title { 
#         font-size: 1.15rem; 
#         font-weight: 800; 
#         background: -webkit-linear-gradient(45deg, #3b82f6, #a855f7); 
#         -webkit-background-clip: text; 
#         -webkit-text-fill-color: transparent; 
#     }
    
#     /* Inputs */
#     .stTextInput > div > div > input, .stSelectbox > div > div > div, .stTextArea > div > div > textarea { 
#         background-color: #0f111a !important; 
#         border: 1px solid rgba(255, 255, 255, 0.08) !important; 
#         color: #e2e8f0 !important; 
#         border-radius: 8px !important; 
#     }
    
#     /* Buttons */
#     div.stButton > button { 
#         background: linear-gradient(135deg, #3b82f6, #a855f7) !important; 
#         color: white !important; 
#         font-weight: 600 !important; 
#         border-radius: 8px !important; 
#         border: none !important; 
#         transition: all 0.3s ease;
#     }
#     div.stButton > button:hover { 
#         transform: translateY(-2px); 
#         box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4) !important; 
#     }
    
#     /* Custom Headings */
#     h1, h2, h3 {
#         font-weight: 800 !important;
#         letter-spacing: -0.5px !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # DISCLAIMER
# DISCLAIMER = "⚠️ **IMPORTANT MEDICAL NOTICE:** This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# # Sidebar
# with st.sidebar:
#     # PDF RAG Style Sidebar Header
#     st.markdown("""
#     <div class="brand-container">
#         <div class="brand-logo">🩺</div>
#         <div style="display: flex; flex-direction: column;">
#             <span class="brand-title">MediGuide AI</span>
#             <span style="font-size: 0.72rem; color: #64748b; font-weight: 500;">AI Symptom Assessment</span>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.error(DISCLAIMER)
    
#     st.markdown("<p style='font-size: 0.72rem; font-weight: 700; color: #475569; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 24px;'>Settings</p>", unsafe_allow_html=True)
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2)
#     enable_caching(cache_option)
#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"])

# # Main Area
# st.markdown("<h1>Patient Symptom Assessment</h1>", unsafe_allow_html=True)
# st.warning(DISCLAIMER)

# # Form Inputs
# with st.form("patient_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Sore Throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 5)
    
#     conditions = st.text_area("Existing Medical Conditions (Optional)")
#     medications = st.text_area("Current Medications (Optional)")
#     notes = st.text_area("Additional Notes (Optional)")
    
#     submitted = st.form_submit_button("✨ Analyse Symptoms", use_container_width=True)

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()
        
#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()
        
#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms, 
#         "duration": duration, "severity": severity, 
#         "conditions": conditions, "medications": medications, 
#         "notes": notes, "language": language
#     }
    
#     st.divider()
#     st.markdown("<h2 style='color: #a855f7;'>🤖 Assessment Dashboard</h2>", unsafe_allow_html=True)
    
#     # Streaming Narrative Section
#     st.markdown("### AI Narrative Analysis")
#     with st.chat_message("assistant", avatar="✨"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
    
#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)
        
#         if result:
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.error(f"🚨 **URGENCY LEVEL: {urgency}** - SEEK IMMEDIATE MEDICAL HELP!")
#             elif "MEDIUM" in urgency:
#                 st.warning(f"⚠️ **URGENCY LEVEL: {urgency}** - Please consult a doctor soon.")
#             else:
#                 st.success(f"🟢 **URGENCY LEVEL: {urgency}** - Monitor symptoms.")
            
#             col_a, col_b = st.columns(2)
            
#             with col_a:
#                 st.info(f"**Summary:** {result.get('summary', '')}")
                
#                 st.markdown("### Possible Conditions (Educational Only)")
#                 for cond in result.get("possible_conditions", []):
#                     st.write(f"- **{cond.get('name')}**: {cond.get('reason')}")
                    
#             with col_b:
#                 st.markdown("### Recommended Next Steps")
#                 for step in result.get("recommended_next_steps", []):
#                     st.write(f"- {step}")
                    
#                 st.markdown("### Warning Signs (Seek Help if seen)")
#                 for sign in result.get("warning_signs", []):
#                     st.write(f"🛑 {sign}")
            
#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)





# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")

# # ==========================================
# # EXACT CYBER-HEALTH THEME (NEON CYAN GLOW)
# # ==========================================
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
#     html, body, [class*="css"] { 
#         font-family: 'Inter', sans-serif !important; 
#         color: #E2E8F0 !important; 
#     }
    
#     /* 1. Deep Dark Background */
#     [data-testid="stAppViewContainer"] {
#         background-color: #050B14 !important;
#         background-image: radial-gradient(circle at 50% 0%, #0a1930 0%, #050b14 70%) !important;
#     }
#     [data-testid="stHeader"] {
#         background-color: transparent !important;
#     }
    
#     /* 2. Sidebar styling */
#     [data-testid="stSidebar"] {
#         background-color: #08101E !important;
#         border-right: 1px solid rgba(0, 242, 254, 0.2) !important;
#         box-shadow: inset -5px 0 20px rgba(0, 242, 254, 0.05) !important;
#     }
    
#     /* 3. Glowing Cyan Input Fields & Dropdowns */
#     .stTextInput > div > div > input,
#     .stSelectbox > div > div > div,
#     .stTextArea > div > div > textarea,
#     .stMultiSelect > div > div > div {
#         background-color: #0A1424 !important;
#         border: 1px solid #00F2FE !important;
#         border-radius: 8px !important;
#         color: #FFFFFF !important;
#         box-shadow: 0 0 10px rgba(0, 242, 254, 0.2) !important;
#         transition: all 0.3s ease !important;
#     }
    
#     /* Hover/Focus effect for inputs */
#     .stTextInput > div > div > input:focus,
#     .stSelectbox > div > div > div:focus,
#     .stTextArea > div > div > textarea:focus {
#         box-shadow: 0 0 15px rgba(0, 242, 254, 0.5) !important;
#         border-color: #4FACFE !important;
#     }

#     /* 4. Multiselect Tags (Like 'Runny nose' in your picture) */
#     span[data-baseweb="tag"] {
#         background-color: rgba(0, 242, 254, 0.15) !important;
#         border: 1px solid #00F2FE !important;
#         color: #00F2FE !important;
#         border-radius: 4px !important;
#     }
    
#     /* 5. Glowing Cyan Button */
#     div.stButton > button {
#         background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%) !important;
#         color: #000000 !important;
#         font-weight: 700 !important;
#         font-size: 16px !important;
#         border: none !important;
#         border-radius: 8px !important;
#         box-shadow: 0 0 15px rgba(0, 242, 254, 0.5) !important;
#         transition: all 0.3s ease !important;
#     }
#     div.stButton > button:hover {
#         box-shadow: 0 0 25px rgba(0, 242, 254, 0.8) !important;
#         transform: scale(1.02) !important;
#     }

#     /* 6. Medical Disclaimer Alert Box (Red Glow) */
#     .stAlert[data-baseweb="notification"] {
#         background-color: rgba(220, 38, 38, 0.05) !important;
#         border: 1px solid rgba(220, 38, 38, 0.4) !important;
#         color: #FCA5A5 !important;
#     }
    
#     /* Headings */
#     h1, h2, h3 {
#         color: #FFFFFF !important;
#         font-weight: 700 !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # DISCLAIMER
# DISCLAIMER = "⚠️ **IMPORTANT MEDICAL NOTICE:** This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# # Sidebar
# with st.sidebar:
#     st.markdown("""
#     <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px;">
#         <div style="font-size: 28px;">🩺</div>
#         <h2 style="margin: 0; color: #00F2FE !important; font-weight: 800;">MediGuide AI</h2>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-bottom: 5px;'>Caching settings</p>", unsafe_allow_html=True)
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2, label_visibility="collapsed")
#     enable_caching(cache_option)
    
#     st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-top: 15px; margin-bottom: 5px;'>Language</p>", unsafe_allow_html=True)
#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"], label_visibility="collapsed")
    
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.error(DISCLAIMER)

# # Main Area
# st.markdown("<h1>Patient Symptom Assessment</h1>", unsafe_allow_html=True)

# # Form Inputs
# with st.form("patient_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age", placeholder="e.g. 25")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Runny nose", "Sore throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 2)
    
#     conditions = st.text_area("Existing Medical Conditions (Optional)", placeholder="Medical notes...")
#     medications = st.text_area("Current Medications (Optional)", placeholder="Medical notes...")
#     notes = st.text_area("Additional Notes (Optional)", placeholder="Medical notes...")
    
#     # Adding spacing before the button to match your picture
#     st.markdown("<br>", unsafe_allow_html=True)
#     submitted = st.form_submit_button("Analyse Symptoms", use_container_width=True)

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()
        
#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()
        
#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms, 
#         "duration": duration, "severity": severity, 
#         "conditions": conditions, "medications": medications, 
#         "notes": notes, "language": language
#     }
    
#     st.divider()
#     st.markdown("<h2 style='color: #00F2FE !important;'>🤖 Assessment Dashboard</h2>", unsafe_allow_html=True)
    
#     # Streaming Narrative Section
#     st.markdown("### AI Narrative Analysis")
#     with st.chat_message("assistant", avatar="✨"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
    
#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)
        
#         if result:
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.error(f"🚨 **URGENCY LEVEL: {urgency}** - SEEK IMMEDIATE MEDICAL HELP!")
#             elif "MEDIUM" in urgency:
#                 st.warning(f"⚠️ **URGENCY LEVEL: {urgency}** - Please consult a doctor soon.")
#             else:
#                 st.success(f"🟢 **URGENCY LEVEL: {urgency}** - Monitor symptoms.")
            
#             col_a, col_b = st.columns(2)
            
#             with col_a:
#                 st.info(f"**Summary:** {result.get('summary', '')}")
                
#                 st.markdown("### Possible Conditions (Educational Only)")
#                 for cond in result.get("possible_conditions", []):
#                     st.write(f"- **{cond.get('name')}**: {cond.get('reason')}")
                    
#             with col_b:
#                 st.markdown("### Recommended Next Steps")
#                 for step in result.get("recommended_next_steps", []):
#                     st.write(f"- {step}")
                    
#                 st.markdown("### Warning Signs (Seek Help if seen)")
#                 for sign in result.get("warning_signs", []):
#                     st.write(f"🛑 {sign}")
            
#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)


# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")

# # ==========================================
# # STRICT CYBER-HEALTH THEME (NEON CYAN GLOW)
# # ==========================================
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
#     html, body, [class*="css"] { 
#         font-family: 'Inter', sans-serif !important; 
#         color: #E2E8F0 !important; 
#     }
    
#     /* 1. Deep Dark Background */
#     [data-testid="stAppViewContainer"] {
#         background-color: #050B14 !important;
#         background-image: radial-gradient(circle at 50% 0%, #0a1930 0%, #050b14 70%) !important;
#     }
#     [data-testid="stHeader"] {
#         background-color: transparent !important;
#     }
    
#     /* 2. Sidebar styling */
#     [data-testid="stSidebar"] {
#         background-color: #08101E !important;
#         border-right: 1px solid rgba(0, 242, 254, 0.2) !important;
#         box-shadow: inset -5px 0 20px rgba(0, 242, 254, 0.05) !important;
#     }
    
#     /* 3. FIX: Form Container Default Border */
#     [data-testid="stForm"] {
#         border: 1px solid rgba(0, 242, 254, 0.1) !important;
#         background-color: rgba(10, 20, 36, 0.3) !important;
#         border-radius: 12px !important;
#         padding: 25px !important;
#         box-shadow: 0 0 15px rgba(0, 0, 0, 0.5) !important;
#     }
    
#     /* 4. Glowing Cyan Input Fields & Dropdowns (Force all states) */
#     div[data-baseweb="input"] > div, 
#     div[data-baseweb="select"] > div, 
#     div[data-baseweb="textarea"] > div {
#         background-color: #0A1424 !important;
#         border: 1px solid rgba(0, 242, 254, 0.6) !important;
#         border-radius: 8px !important;
#         box-shadow: 0 0 8px rgba(0, 242, 254, 0.15) !important;
#     }
    
#     /* Input Text Color */
#     input, textarea, div[data-baseweb="select"] span {
#         color: #FFFFFF !important;
#     }
    
#     /* Hover/Focus effect */
#     div[data-baseweb="input"] > div:hover, 
#     div[data-baseweb="select"] > div:hover, 
#     div[data-baseweb="textarea"] > div:hover {
#         border: 1px solid #00F2FE !important;
#         box-shadow: 0 0 15px rgba(0, 242, 254, 0.4) !important;
#     }

#     /* 5. FIX: Multiselect Tags Color (Force Cyan instead of Red) */
#     span[data-baseweb="tag"] {
#         background-color: rgba(0, 242, 254, 0.15) !important;
#         border: 1px solid #00F2FE !important;
#         color: #00F2FE !important;
#         border-radius: 4px !important;
#     }
#     span[data-baseweb="tag"] span {
#         color: #00F2FE !important;
#     }
    
#     /* 6. FIX: Slider Color (Force Cyan instead of Red) */
#     div[data-baseweb="slider"] div[role="slider"] {
#         background-color: #00F2FE !important;
#         border: 2px solid #FFFFFF !important;
#         box-shadow: 0 0 12px #00F2FE !important;
#     }
#     div[data-baseweb="slider"] div {
#         background-color: rgba(0, 242, 254, 0.8) !important;
#     }
    
#     /* 7. Glowing Cyan Button */
#     div.stButton > button {
#         background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%) !important;
#         color: #000000 !important;
#         font-weight: 700 !important;
#         font-size: 16px !important;
#         border: none !important;
#         border-radius: 8px !important;
#         box-shadow: 0 0 15px rgba(0, 242, 254, 0.5) !important;
#         transition: all 0.3s ease !important;
#     }
#     div.stButton > button:hover {
#         box-shadow: 0 0 25px rgba(0, 242, 254, 0.8) !important;
#         transform: scale(1.02) !important;
#     }

#     /* 8. Medical Disclaimer Alert Box (Red Glow) */
#     .stAlert[data-baseweb="notification"] {
#         background-color: rgba(220, 38, 38, 0.05) !important;
#         border: 1px solid rgba(220, 38, 38, 0.4) !important;
#         color: #FCA5A5 !important;
#     }
    
#     /* Headings */
#     h1, h2, h3 {
#         color: #FFFFFF !important;
#         font-weight: 700 !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # DISCLAIMER
# DISCLAIMER = "⚠️ **IMPORTANT MEDICAL NOTICE:** This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# # Sidebar
# with st.sidebar:
#     st.markdown("""
#     <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px;">
#         <div style="font-size: 28px;">🩺</div>
#         <h2 style="margin: 0; color: #00F2FE !important; font-weight: 800;">MediGuide AI</h2>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-bottom: 5px;'>Caching settings</p>", unsafe_allow_html=True)
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2, label_visibility="collapsed")
#     enable_caching(cache_option)
    
#     st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-top: 15px; margin-bottom: 5px;'>Language</p>", unsafe_allow_html=True)
#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"], label_visibility="collapsed")
    
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.error(DISCLAIMER)

# # Main Area
# st.markdown("<h1>Patient Symptom Assessment</h1>", unsafe_allow_html=True)

# # Form Inputs
# with st.form("patient_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age", placeholder="e.g. 25")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Runny nose", "Sore throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 2)
    
#     conditions = st.text_area("Existing Medical Conditions (Optional)", placeholder="Medical notes...")
#     medications = st.text_area("Current Medications (Optional)", placeholder="Medical notes...")
#     notes = st.text_area("Additional Notes (Optional)", placeholder="Medical notes...")
    
#     st.markdown("<br>", unsafe_allow_html=True)
#     submitted = st.form_submit_button("Analyse Symptoms", use_container_width=True)

# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()
        
#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()
        
#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms, 
#         "duration": duration, "severity": severity, 
#         "conditions": conditions, "medications": medications, 
#         "notes": notes, "language": language
#     }
    
#     st.divider()
#     st.markdown("<h2 style='color: #00F2FE !important;'>🤖 Assessment Dashboard</h2>", unsafe_allow_html=True)
    
#     # Streaming Narrative Section
#     st.markdown("### AI Narrative Analysis")
#     with st.chat_message("assistant", avatar="✨"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
    
#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)
        
#         if result:
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.error(f"🚨 **URGENCY LEVEL: {urgency}** - SEEK IMMEDIATE MEDICAL HELP!")
#             elif "MEDIUM" in urgency:
#                 st.warning(f"⚠️ **URGENCY LEVEL: {urgency}** - Please consult a doctor soon.")
#             else:
#                 st.success(f"🟢 **URGENCY LEVEL: {urgency}** - Monitor symptoms.")
            
#             col_a, col_b = st.columns(2)
            
#             with col_a:
#                 st.info(f"**Summary:** {result.get('summary', '')}")
                
#                 st.markdown("### Possible Conditions (Educational Only)")
#                 for cond in result.get("possible_conditions", []):
#                     st.write(f"- **{cond.get('name')}**: {cond.get('reason')}")
                    
#             with col_b:
#                 st.markdown("### Recommended Next Steps")
#                 for step in result.get("recommended_next_steps", []):
#                     st.write(f"- {step}")
                    
#                 st.markdown("### Warning Signs (Seek Help if seen)")
#                 for sign in result.get("warning_signs", []):
#                     st.write(f"🛑 {sign}")
            
#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)




# import streamlit as st
# import os
# from dotenv import load_dotenv
# from src.cache_manager import enable_caching
# from src.utils import parse_json_safely
# from src.chains import get_assessment_chain, stream_narrative

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# st.set_page_config(
#     page_title="MediGuide AI",
#     page_icon="🩺",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ---------------------------------------------------------------------------
# # CUSTOM CSS — gives the app a polished, "built by an AI engineer" look
# # ---------------------------------------------------------------------------
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

#     html, body, [class*="css"]  {
#         font-family: 'Inter', sans-serif;
#     }

#     /* App background */
#     .stApp {
#         background: radial-gradient(circle at top left, #0f1b2d 0%, #0a0e1a 45%, #05070d 100%);
#     }

#     /* Hero header */
#     .hero-banner {
#         background: linear-gradient(120deg, #0ea5e9 0%, #6366f1 50%, #a855f7 100%);
#         padding: 2.2rem 2.5rem;
#         border-radius: 20px;
#         margin-bottom: 1.6rem;
#         box-shadow: 0 15px 35px -10px rgba(99, 102, 241, 0.45);
#         position: relative;
#         overflow: hidden;
#     }
#     .hero-banner::after {
#         content: "";
#         position: absolute;
#         top: -40%; right: -10%;
#         width: 260px; height: 260px;
#         background: rgba(255,255,255,0.12);
#         border-radius: 50%;
#     }
#     .hero-title {
#         color: white;
#         font-size: 2.3rem;
#         font-weight: 800;
#         margin: 0;
#         letter-spacing: -0.5px;
#     }
#     .hero-subtitle {
#         color: rgba(255,255,255,0.88);
#         font-size: 1.02rem;
#         margin-top: 0.4rem;
#         font-weight: 500;
#     }
#     .hero-badge {
#         display: inline-block;
#         background: rgba(255,255,255,0.18);
#         color: white;
#         padding: 4px 14px;
#         border-radius: 999px;
#         font-size: 0.75rem;
#         font-weight: 600;
#         margin-top: 0.9rem;
#         backdrop-filter: blur(6px);
#         border: 1px solid rgba(255,255,255,0.3);
#     }

#     /* Disclaimer card */
#     .disclaimer-card {
#         background: linear-gradient(135deg, rgba(239,68,68,0.12), rgba(239,68,68,0.04));
#         border: 1px solid rgba(239,68,68,0.35);
#         border-left: 5px solid #ef4444;
#         border-radius: 14px;
#         padding: 1rem 1.3rem;
#         color: #fecaca;
#         font-size: 0.9rem;
#         line-height: 1.5;
#         margin-bottom: 1.2rem;
#     }
#     .disclaimer-card b { color: #fca5a5; }

#     /* Section card wrapper */
#     .glass-card {
#         background: rgba(255,255,255,0.035);
#         border: 1px solid rgba(255,255,255,0.08);
#         border-radius: 18px;
#         padding: 1.8rem 2rem;
#         backdrop-filter: blur(10px);
#         box-shadow: 0 10px 30px -15px rgba(0,0,0,0.6);
#         margin-bottom: 1.3rem;
#     }

#     .section-heading {
#         color: #e2e8f0;
#         font-weight: 700;
#         font-size: 1.15rem;
#         margin-bottom: 0.9rem;
#         display: flex;
#         align-items: center;
#         gap: 8px;
#     }

#     /* Inputs */
#     .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
#         background-color: rgba(255,255,255,0.05) !important;
#         border: 1px solid rgba(255,255,255,0.12) !important;
#         border-radius: 10px !important;
#         color: #f1f5f9 !important;
#     }
#     .stTextInput input:focus, .stTextArea textarea:focus {
#         border-color: #6366f1 !important;
#         box-shadow: 0 0 0 2px rgba(99,102,241,0.25) !important;
#     }

#     /* Slider */
#     .stSlider [data-baseweb="slider"] > div > div {
#         background: linear-gradient(90deg, #0ea5e9, #a855f7) !important;
#     }

#     /* Submit button */
#     .stFormSubmitButton button, .stButton button {
#         background: linear-gradient(120deg, #0ea5e9, #6366f1, #a855f7);
#         color: white;
#         font-weight: 700;
#         border: none;
#         border-radius: 12px;
#         padding: 0.7rem 1.4rem;
#         letter-spacing: 0.3px;
#         box-shadow: 0 8px 20px -8px rgba(99,102,241,0.6);
#         transition: transform 0.15s ease, box-shadow 0.15s ease;
#     }
#     .stFormSubmitButton button:hover, .stButton button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 12px 26px -8px rgba(99,102,241,0.75);
#     }

#     /* Urgency banners */
#     .urgency-box {
#         border-radius: 14px;
#         padding: 1rem 1.3rem;
#         font-weight: 700;
#         font-size: 1.02rem;
#         margin: 1rem 0 1.4rem 0;
#         border: 1px solid;
#     }
#     .urgency-high {
#         background: rgba(239,68,68,0.12);
#         border-color: rgba(239,68,68,0.45);
#         color: #fca5a5;
#     }
#     .urgency-medium {
#         background: rgba(245,158,11,0.12);
#         border-color: rgba(245,158,11,0.45);
#         color: #fcd34d;
#     }
#     .urgency-low {
#         background: rgba(34,197,94,0.12);
#         border-color: rgba(34,197,94,0.45);
#         color: #86efac;
#     }

#     /* Result item cards */
#     .result-item {
#         background: rgba(255,255,255,0.04);
#         border: 1px solid rgba(255,255,255,0.08);
#         border-radius: 12px;
#         padding: 0.75rem 1rem;
#         margin-bottom: 0.6rem;
#         color: #e2e8f0;
#         font-size: 0.93rem;
#     }
#     .result-item b { color: #93c5fd; }

#     .warning-item {
#         background: rgba(239,68,68,0.08);
#         border: 1px solid rgba(239,68,68,0.3);
#         border-radius: 12px;
#         padding: 0.65rem 1rem;
#         margin-bottom: 0.55rem;
#         color: #fecaca;
#         font-size: 0.92rem;
#     }

#     /* Sidebar */
#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #0b1220 0%, #0a0e1a 100%);
#         border-right: 1px solid rgba(255,255,255,0.06);
#     }
#     .sidebar-title {
#         color: #f1f5f9;
#         font-weight: 800;
#         font-size: 1.4rem;
#     }
#     .sidebar-caption {
#         color: #94a3b8;
#         font-size: 0.85rem;
#         margin-bottom: 1rem;
#     }

#     footer {visibility: hidden;}
#     #MainMenu {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # DISCLAIMER (plain text version used for logic, HTML version used for display)
# DISCLAIMER_TEXT = "This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# def render_disclaimer():
#     st.markdown(f"""
#     <div class="disclaimer-card">
#         ⚠️ <b>IMPORTANT MEDICAL NOTICE:</b> {DISCLAIMER_TEXT}
#     </div>
#     """, unsafe_allow_html=True)

# # ---------------------------------------------------------------------------
# # SIDEBAR
# # ---------------------------------------------------------------------------
# with st.sidebar:
#     st.markdown('<div class="sidebar-title">🩺 MediGuide AI</div>', unsafe_allow_html=True)
#     st.markdown('<div class="sidebar-caption">AI-Powered Medical Symptom Assessment</div>', unsafe_allow_html=True)

#     render_disclaimer()

#     st.markdown("#### ⚙️ Settings")
#     cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"])
#     enable_caching(cache_option)

#     language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"])

#     st.markdown("---")
#     st.caption("Built with ❤️ using LangChain + OpenAI")

# # ---------------------------------------------------------------------------
# # HERO / HEADER
# # ---------------------------------------------------------------------------
# st.markdown("""
# <div class="hero-banner">
#     <div class="hero-title">Patient Symptom Assessment</div>
#     <div class="hero-subtitle">Describe your symptoms below and get an instant, AI-generated educational health overview.</div>
#     <div class="hero-badge">⚡ Powered by Generative AI</div>
# </div>
# """, unsafe_allow_html=True)

# render_disclaimer()

# # ---------------------------------------------------------------------------
# # FORM
# # ---------------------------------------------------------------------------
# st.markdown('<div class="glass-card">', unsafe_allow_html=True)
# with st.form("patient_form"):
#     st.markdown('<div class="section-heading">📝 Patient Details</div>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.text_input("Patient Age")
#         gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
#         duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
#     with col2:
#         symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Sore Throat"])
#         other_symptoms = st.text_input("Other Symptoms (if any)")
#         severity = st.slider("Severity Level (1-10)", 1, 10, 5)

#     st.markdown('<div class="section-heading" style="margin-top:0.8rem;">🩹 Medical Background (Optional)</div>', unsafe_allow_html=True)
#     conditions = st.text_area("Existing Medical Conditions")
#     medications = st.text_area("Current Medications")
#     notes = st.text_area("Additional Notes")

#     submitted = st.form_submit_button("🔍 Analyse Symptoms", type="primary")
# st.markdown('</div>', unsafe_allow_html=True)

# # ---------------------------------------------------------------------------
# # RESULTS
# # ---------------------------------------------------------------------------
# if submitted:
#     if not API_KEY:
#         st.error("API Key is missing! Please add it to your .env file.")
#         st.stop()

#     if not symptoms and not other_symptoms:
#         st.error("Please provide at least one symptom.")
#         st.stop()

#     all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")

#     inputs = {
#         "age": age, "gender": gender, "symptoms": all_symptoms,
#         "duration": duration, "severity": severity,
#         "conditions": conditions, "medications": medications,
#         "notes": notes, "language": language
#     }

#     st.markdown("<br>", unsafe_allow_html=True)
#     st.markdown("""
#     <div class="hero-banner" style="padding:1.3rem 2rem;">
#         <div class="hero-title" style="font-size:1.5rem;">🤖 Assessment Dashboard</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Streaming Narrative Section
#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#     st.markdown('<div class="section-heading">💬 AI Narrative Analysis</div>', unsafe_allow_html=True)
#     with st.chat_message("assistant"):
#         st.write_stream(stream_narrative(API_KEY, inputs))
#     st.markdown('</div>', unsafe_allow_html=True)

#     # JSON Data Processing
#     with st.spinner("Generating structured medical guidance..."):
#         chain = get_assessment_chain(API_KEY)
#         raw_output = chain.invoke(inputs)
#         result = parse_json_safely(raw_output)

#         if result:
#             # Urgency Level Logic
#             urgency = result.get("urgency_level", "UNKNOWN").upper()
#             if "EMERGENCY" in urgency or "HIGH" in urgency:
#                 st.markdown(f'<div class="urgency-box urgency-high">🚨 URGENCY LEVEL: {urgency} — SEEK IMMEDIATE MEDICAL HELP!</div>', unsafe_allow_html=True)
#             elif "MEDIUM" in urgency:
#                 st.markdown(f'<div class="urgency-box urgency-medium">⚠️ URGENCY LEVEL: {urgency} — Please consult a doctor soon.</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="urgency-box urgency-low">🟢 URGENCY LEVEL: {urgency} — Monitor symptoms.</div>', unsafe_allow_html=True)

#             st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#             st.markdown('<div class="section-heading">📋 Summary</div>', unsafe_allow_html=True)
#             st.markdown(f'<div class="result-item">{result.get("summary", "")}</div>', unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)

#             col_a, col_b = st.columns(2)

#             with col_a:
#                 st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#                 st.markdown('<div class="section-heading">🧬 Possible Conditions</div>', unsafe_allow_html=True)
#                 st.caption("Educational only — not a diagnosis")
#                 for cond in result.get("possible_conditions", []):
#                     st.markdown(f'<div class="result-item"><b>{cond.get("name")}</b>: {cond.get("reason")}</div>', unsafe_allow_html=True)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with col_b:
#                 st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#                 st.markdown('<div class="section-heading">✅ Recommended Next Steps</div>', unsafe_allow_html=True)
#                 for step in result.get("recommended_next_steps", []):
#                     st.markdown(f'<div class="result-item">{step}</div>', unsafe_allow_html=True)

#                 st.markdown('<div class="section-heading" style="margin-top:1rem;">🛑 Warning Signs</div>', unsafe_allow_html=True)
#                 for sign in result.get("warning_signs", []):
#                     st.markdown(f'<div class="warning-item">🛑 {sign}</div>', unsafe_allow_html=True)
#                 st.markdown('</div>', unsafe_allow_html=True)

#             with st.expander("❓ Questions to ask your Doctor"):
#                 for q in result.get("questions_for_doctor", []):
#                     st.write(f"- {q}")
#         else:
#             st.error("Failed to parse AI response. Please try again.")
#             st.code(raw_output)


import streamlit as st
import os
from dotenv import load_dotenv
from src.cache_manager import enable_caching
from src.utils import parse_json_safely
from src.chains import get_assessment_chain, stream_narrative

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="MediGuide AI", page_icon="🩺", layout="wide")

# Streamlit ke default Header (Fork/GitHub) aur Footer ko hide karne ka CSS
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# GLOWING NEON CSS (Works with config.toml)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif !important; 
    }
    
    /* Radial Gradient Background */
    [data-testid="stAppViewContainer"] {
        background-image: radial-gradient(circle at 50% 0%, #0a1930 0%, #050b14 70%) !important;
    }
    
    /* Glowing Inputs */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div,
    .stTextArea > div > div > textarea,
    .stMultiSelect > div > div > div {
        background-color: rgba(10, 20, 36, 0.8) !important;
        border: 1px solid #00F2FE !important;
        border-radius: 8px !important;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15) !important;
    }
    
    /* Form Background */
    [data-testid="stForm"] {
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Glowing Cyan Button */
    div[data-testid="stFormSubmitButton"] > button, .stButton > button {
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%) !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 8px !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.6) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover {
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.9) !important;
        transform: scale(1.02) !important;
    }
    
    /* Tags styling */
    span[data-baseweb="tag"] {
        background-color: rgba(0, 242, 254, 0.2) !important;
        border: 1px solid #00F2FE !important;
    }
</style>
""", unsafe_allow_html=True)

# DISCLAIMER
DISCLAIMER = "⚠️ **IMPORTANT MEDICAL NOTICE:** This application is an educational AI prototype ONLY. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. Please consult a qualified healthcare professional and seek emergency help in urgent situations."

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px;">
        <div style="font-size: 28px;">🩺</div>
        <h2 style="margin: 0; color: #00F2FE !important; font-weight: 800;">MediGuide AI</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-bottom: 5px;'>Caching settings</p>", unsafe_allow_html=True)
    cache_option = st.selectbox("Caching System", ["None", "In-Memory", "SQLite"], index=2, label_visibility="collapsed")
    enable_caching(cache_option)
    
    st.markdown("<p style='font-size: 0.8rem; font-weight: 600; color: #E2E8F0; margin-top: 15px; margin-bottom: 5px;'>Language</p>", unsafe_allow_html=True)
    language = st.selectbox("Output Language", ["English", "Urdu", "Hindi"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.error(DISCLAIMER)

# Main Area
st.markdown("<h1>Patient Symptom Assessment</h1>", unsafe_allow_html=True)

# Form Inputs
with st.form("patient_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.text_input("Patient Age", placeholder="e.g. 25")
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        duration = st.selectbox("Symptom Duration", ["Less than 1 day", "1-3 days", "4-7 days", "More than a week", "More than a month"])
    with col2:
        symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Headache", "Chest Pain", "Shortness of Breath", "Fatigue", "Nausea", "Runny nose", "Sore throat"])
        other_symptoms = st.text_input("Other Symptoms (if any)")
        severity = st.slider("Severity Level (1-10)", 1, 10, 2)
    
    conditions = st.text_area("Existing Medical Conditions (Optional)", placeholder="Medical notes...")
    medications = st.text_area("Current Medications (Optional)", placeholder="Medical notes...")
    notes = st.text_area("Additional Notes (Optional)", placeholder="Medical notes...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    # Button changed to type="primary" to link with config.toml
    submitted = st.form_submit_button("Analyse Symptoms", type="primary", use_container_width=True)

if submitted:
    if not API_KEY:
        st.error("API Key is missing! Please add it to your .env file.")
        st.stop()
        
    if not symptoms and not other_symptoms:
        st.error("Please provide at least one symptom.")
        st.stop()
        
    all_symptoms = ", ".join(symptoms) + (" " + other_symptoms if other_symptoms else "")
    
    inputs = {
        "age": age, "gender": gender, "symptoms": all_symptoms, 
        "duration": duration, "severity": severity, 
        "conditions": conditions, "medications": medications, 
        "notes": notes, "language": language
    }
    
    st.divider()
    st.markdown("<h2 style='color: #00F2FE !important;'>🤖 Assessment Dashboard</h2>", unsafe_allow_html=True)
    
    # Streaming Narrative Section
    st.markdown("### AI Narrative Analysis")
    with st.chat_message("assistant", avatar="✨"):
        st.write_stream(stream_narrative(API_KEY, inputs))
    
    # JSON Data Processing
    with st.spinner("Generating structured medical guidance..."):
        chain = get_assessment_chain(API_KEY)
        raw_output = chain.invoke(inputs)
        result = parse_json_safely(raw_output)
        
        if result:
            urgency = result.get("urgency_level", "UNKNOWN").upper()
            if "EMERGENCY" in urgency or "HIGH" in urgency:
                st.error(f"🚨 **URGENCY LEVEL: {urgency}** - SEEK IMMEDIATE MEDICAL HELP!")
            elif "MEDIUM" in urgency:
                st.warning(f"⚠️ **URGENCY LEVEL: {urgency}** - Please consult a doctor soon.")
            else:
                st.success(f"🟢 **URGENCY LEVEL: {urgency}** - Monitor symptoms.")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.info(f"**Summary:** {result.get('summary', '')}")
                
                st.markdown("### Possible Conditions (Educational Only)")
                for cond in result.get("possible_conditions", []):
                    st.write(f"- **{cond.get('name')}**: {cond.get('reason')}")
                    
            with col_b:
                st.markdown("### Recommended Next Steps")
                for step in result.get("recommended_next_steps", []):
                    st.write(f"- {step}")
                    
                st.markdown("### Warning Signs (Seek Help if seen)")
                for sign in result.get("warning_signs", []):
                    st.write(f"🛑 {sign}")
            
            with st.expander("❓ Questions to ask your Doctor"):
                for q in result.get("questions_for_doctor", []):
                    st.write(f"- {q}")
        else:
            st.error("Failed to parse AI response. Please try again.")
            st.code(raw_output)


