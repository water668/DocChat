import os

from langchain_ollama import ChatOllama
llm_qwen35_2b = ChatOllama(model="qwen3.5:2b", temperature=0.3)

from langchain_deepseek.chat_models import ChatDeepSeek
llm_deepseek_chat = ChatDeepSeek(model="deepseek-chat", temperature=0.3, api_key=os.environ['DEEPSEEK_API_KEY'], base_url='https://api.deepseek.com/v1')

def get_llm(model='qwen3.5:2b'):
    if model == 'qwen3.5:2b':
        return llm_qwen35_2b
    elif model == 'deepseek-chat':
        return llm_deepseek_chat
    else:
        raise ValueError(f"Unsupported LLM model: {model}")

