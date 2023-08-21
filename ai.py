import os

import openai
from dotenv import load_dotenv

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")

def preprocess_input(input_text):
    prompt = f"""You are a library assistant. If the question relies on library-specific data, return 'FLAG'.
Otherwise, answer the question based on context:
{input_text}
     
If the input is not a valid question, return 'I don't understand'."""
    return prompt

def get_response(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=preprocess_input(input_text),
        temperature=0.6,
        max_tokens=100,
    )

    return response.choices[0].text.strip()
