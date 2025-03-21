# -*- coding: utf-8 -*-
"""FDP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W4K7tULGcbMhA81W9HOO79yMugphoeTL
"""

pip install groq

import os
from groq import Groq

def ask_question(api_key):
    """Ask a straightforward question to the Groq API."""
    client = Groq(api_key=api_key)
    question = "What are the top 3 most interesting tings in cmr college of engineering & technology?"
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="mixtral-8x7b-32768"
    )

    print("Question:", question)
    print("\nResponse:", response.choices[0].message.content)

def main():
    api_key = "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"
    ask_question(api_key)

if __name__ == "__main__":
    main()

import os
from groq import Groq

def ask_question(api_key, question):
    """Ask a question to the Groq API."""
    client = Groq(api_key=api_key)
    system_prompt = """consider you are the best doctor in world help this question."""
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        model="mixtral-8x7b-32768"
    )

    print("\nResponse:", response.choices[0].message.content)

def main():
    api_key = "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"
    question = input("Enter your question: ")
    ask_question(api_key, question)

if __name__ == "__main__":
    main()

pip install llama-index-llms-groq

pip install llama-index

from llama_index.llms.groq import Groq

GROQ_API_KEY="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"

!pip install --upgrade llama-index-llms-groq

llm = Groq(model="llama3-70b-8192", api_key="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")

response = llm.complete("Explain the important of low latency LLMs")

print(response)

from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user",content="what is your name")
]
resp = llm.chat(messages)



print(resp)

response = llm.stream_complete("Explain the importance of low latency LLMS")

for r in response:
  print(r.delta, end="")

pip install llama-index llama-index-embeddings-huggingface llama-index-llms-groq

import logging
import sys
from google.colab import userdata
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.openai import OpenAI
from llama_index.llms.groq import Groq

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

!mkdir data
!wget -O data/essay.txt https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt

documents = SimpleDirectoryReader("data").load_data()

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

GROQ_API_KEY = "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"

# os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')

# llm = OpenAI(
#     model="gpt-3.5-turbo",
#     api_key=userdata.get('sk-o60aCUo7BIVicqzB9moWRGmmqi1cipD_DxNfLgYvdRT3BlbkFJBEdMcAOAsfbQoVnuEbEMDBjEm8WMrz16hteNIyjqUA')
# )

llm = Groq(
   model="llama3-70b-8192",
   api_key="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"
)

Settings.embed_model = embed_model
Settings.llm = llm

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("What did the author do growing up?")
print(response)