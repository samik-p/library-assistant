import os

import openai
from dotenv import load_dotenv
from classify import *

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_scenario_prompt(input_text):
    prompt = f"""If the question relies on library-specific data or is not a valid question, return 'FLAG'.
Otherwise, answer the question based on context:
{input_text}"""

    return prompt


def get_response(input_text):
    classification = classify_input(input_text)

    print(f"<cohere> {classification}")
    if classification == "See librarian":
        call_librarian(input_text)

        return "Calling a librarian to help you."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a library assistant."},
            {"role": "user", "content": generate_scenario_prompt(input_text)},
        ],
        max_tokens=50,
    )

    if "choices" in response and len(response["choices"]) > 0:
        output_text = response["choices"][0]["message"]["content"]
    else:
        print("No response from the assistant.")

    if "FLAG" in output_text:
        print("<gpt-3.5-turbo> FLAG")

        call_librarian(input_text)

        return "Calling a librarian to help you."

    return output_text


def call_librarian(input_text):
    backup_prompt = f"A patron just asked: '{input_text}'. Summarize this question and generate a short report for the librarian."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a library assistant."},
            {"role": "user", "content": input_text},
            # {"role": "assistant", "content": output_text},
            {"role": "user", "content": backup_prompt},
        ],
        max_tokens=50,
    )
    if "choices" in response and len(response["choices"]) > 0:
        message = response["choices"][0]["message"]["content"]
    else:
        print(f"(No response from the assistant) - USER: {input_text}")

    print(f"=========\nSENT TO LIBRARIAN: {message}\n=========")


def process_librarian_response(answer_text, original_question):
    prompt = f"""Clarify the following input:
{answer_text}"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a library assistant."},
            {"role": "user", "content": original_question},
            {"role": "assistant", "content": answer_text},
            {"role": "user", "content": prompt},
        ],
        max_tokens=50,
    )
    if "choices" in response and len(response["choices"]) > 0:
        message = response["choices"][0]["message"]["content"]
    else:
        message = f"(No response from the assistant) - {answer_text}"

    return message
