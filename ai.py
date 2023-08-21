import os

import openai
from dotenv import load_dotenv
from classify import *

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")


# generate the initial scenario prompt for a user message
def generate_scenario_prompt(input_text):
    prompt = f"""Respond to the following based on prior context:
{input_text}"""
    return prompt


# handle the initial response from USER
def get_response(input_text, examples):
    # classify input text as either
    # 1. "Answer"        : something the AI can help with immediately,
    # 2. "See librarian" : something requiring librarian assistance,
    # 3. "Conversation"  : other conversation
    classification = classify_input(input_text, examples)

    append_example_to_file("examples.txt", input_text, classification)

    print(f"<cohere> {classification}")

    # case #2
    if classification == "See librarian":
        # sends a summary to the librarian and outputs that a librarian has been called
        call_librarian(input_text)
        return "Calling a librarian to help you."

    # generate a response based on input query using text generation from LLM
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a library assistant."},
            {"role": "user", "content": generate_scenario_prompt(input_text)},
        ],
        max_tokens=50,
    )

    # verifies that LLM did not error and responded with a list of choice responses
    if "choices" in response and len(response["choices"]) > 0:
        output_text = response["choices"][0]["message"]["content"]
    else:
        print("No response from the assistant.")

    return output_text


# generates a summary of patron query to provide to librarian
def call_librarian(input_text):
    # prompt engineering
    backup_prompt = f"A patron just asked: '{input_text}'. Summarize this question for the librarian."

    # generate summary of input query using LLM
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

    # verifies that LLM did not error and responded with a list of choice responses
    if "choices" in response and len(response["choices"]) > 0:
        message = response["choices"][0]["message"]["content"]
    else:
        print(f"(No response from the assistant) - USER: {input_text}")

    # indicate that report has been sent to librarian
    print(f"=========\nSENT TO LIBRARIAN: {message}\n=========")


# takes (possibly shortened) librarian input and generates a cleaned response to give back to patron
def process_librarian_response(answer_text, original_question):
    prompt = f"""Clarify the following input:
{answer_text}"""

    # generate summary of input query using LLM
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

    # verifies that LLM did not error and responded with a list of choice responses
    if "choices" in response and len(response["choices"]) > 0:
        message = response["choices"][0]["message"]["content"]
    else:
        message = f"(No response from the assistant) - {answer_text}"

    return message
