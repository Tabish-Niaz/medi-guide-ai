from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from src.prompts import chat_prompt, narrative_chat_prompt

def get_assessment_chain(api_key):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=api_key)
    return chat_prompt | llm | StrOutputParser()

def stream_narrative(api_key, inputs):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=api_key)
    messages = narrative_chat_prompt.format_messages(**inputs)
    for chunk in llm.stream(messages):
        if chunk.content:
            yield chunk.content