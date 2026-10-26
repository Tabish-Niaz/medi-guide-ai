## MediGuide AI: AI-Powered Medical Symptom Assessment and Patient Guidance Assistant

MediGuide AI is an educational healthcare web application built using Streamlit and LangChain. It combines patient symptom inputs and medical contexts with structured, safety-focused educational guidance powered by OpenAI (gpt-4o-mini).

⚠️ IMPORTANT MEDICAL & SAFETY NOTICE: This application is an educational AI prototype only. It is NOT a replacement for a licensed doctor, professional diagnosis, emergency service, or medical treatment. It must never present a confirmed diagnosis. Every screen directs users to consult a qualified healthcare professional and seek emergency help in urgent situations.

## 🚀 Features

1. Structured Medical Assessments: Collects patient age, gender, multi-select symptoms, duration, severity ratings (1-10), medical history, medications, and notes.

2. Safety-First AI Guidance: Leverages LangChain prompts and ChatOpenAI to return strict JSON schema containing urgency levels, summary, possible educational conditions, warning signs, and doctor questions.

3. Live Streaming Narrative: Streams safety-focused preliminary guidance dynamically onto the UI for a natural typing effect.

4. Flexible Caching: Supports both In-Memory (InMemoryCache) and Disk-based (SQLiteCache) caching to optimize response speed and reduce redundant API calls.

5. Multilingual Support: Allows users to request guidance in multiple languages (English, Urdu, Hindi).


## 📂 Project Folder Structure

Medi Guide AI/
│
├── app.py                  # Main Streamlit UI application
├── requirements.txt        # Project dependencies
├── .env           # Environment variables template
├── README.md               # Project documentation
└── src/
    ├── __init__.py
    ├── config.py           # Settings and configuration options
    ├── prompts.py          # System prompts & JSON schema templates
    ├── chains.py           # LangChain integration & streaming
    ├── cache_manager.py    # In-Memory & SQLite caching setup
    └── utils.py            # Safe JSON parsing helpers


🛠️ Setup and Installation Instructions

1. Clone the Repository:

git clone https://github.com/Tabish-Niaz/medi-guide-ai.git
cd medi-guide-ai


2. Create a Virtual Environment (Python 3.10+ Recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


3. Install Dependencies:

pip install -r requirements.txt


4. Configure Environment Variables:

Copy the .env file to create a new file named .env:

cp .env .env


5. Open .env and add your OpenAI API key:

OPENAI_API_KEY="sk-proj-your-api-key-here"


6. Run the Application:

streamlit run app.py


🧠 Technical Architecture & Explanations

1. Safety Guardrails & Structured Prompting (prompts.py)

System Guardrails: 
Strict safety rules are hardcoded into the system message template to ensure the AI never claims a confirmed diagnosis and always emphasizes professional medical consultation.

Structured JSON Schema: 
Forces the LLM to output predictable keys (summary, urgency_level, possible_conditions, recommended_next_steps, warning_signs, questions_for_doctor) which are safely parsed using utils.py to prevent any app crashes from malformed outputs.

2. Caching Implementation (cache_manager.py)

To prevent redundant API costs and lower latency, MediGuide AI integrates LangChain's global caching mechanism (set_llm_cache):

InMemoryCache: 
Stores responses temporarily in RAM. Best for single active session performance.

SQLiteCache: 
Persists responses to a local .langchain_cache.db file on disk, surviving application restarts across multiple runs.