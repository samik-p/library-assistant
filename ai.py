import os

import openai
from dotenv import load_dotenv

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_scenario_prompt(input_text):
    prompt = f"""You are a library assistant. If the question relies on library-specific data, return 'FLAG'.
Otherwise, answer the question based on context:
{input_text}
     
If the input is not a valid question, return 'I don't understand'."""
    return prompt

def get_response(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_scenario_prompt(input_text),
        temperature=0.6,
        max_tokens=100,
    )

    output_text = response.choices[0].text.strip()

    if "FLAG" in output_text:

        call_librarian(input_text)

        return "Calling a librarian to help you."

    return output_text

def call_librarian(input_text):

    # call a librarian and
    # send the input text for context

    backup_prompt = f"A patron just asked: '{input_text}'. Summarize this question and generate a short report for the librarian."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=backup_prompt,
        temperature=0.6,
        max_tokens=100,
    )
    message = response.choices[0].text.strip()

    print(f"=========\nSENT TO LIBRARIAN: {message}\n=========")


def process_librarian_response(answer_text, original_question):

    prompt = f"""Clarify the following input:
{answer_text}

This was original question for context:
{original_question}
"""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100,
    )
    message = response.choices[0].text.strip()

    return message
    