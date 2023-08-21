import os

import openai
from dotenv import load_dotenv

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input_text,
        temperature=0.6,
        max_tokens=100,
    )

    return response.choices[0].text.strip()
