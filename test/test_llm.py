
import sys

import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.llm import get_llm

if __name__ == '__main__':
    llm = get_llm('qwen3.5:2b')
    response = llm.invoke("What is the capital of France?")
    print('response[qwen3.5:2b]:',response)
    llm = get_llm('deepseek-chat')
    response = llm.invoke("What is the capital of France?")
    print('response[deepseek-chat]:',response)
