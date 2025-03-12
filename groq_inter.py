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
