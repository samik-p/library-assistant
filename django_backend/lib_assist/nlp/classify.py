import os

import cohere
from re import match
from cohere.responses.classify import Example
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_CLIENT"))


def parse_file_for_examples(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            components = match(r'"(.*?)"\s*,\s*"([^"]*)"', line)
            if components:
                sentence, label = components.group(1), components.group(2)
                data.append(Example(sentence, label))
    return data


def append_example_to_file(filename, input, classification):
    with open(filename, "a") as file:
        file.write(f'\n"{input}", "{classification}"')
        # examples.append(Example(input, classification))
        print(f'OK: added <"{input}", "{classification}"> to {filename}')

        file.close()


def classify_input(input_text, examples):
    # response format:
    # list of Classification objects (length 1)
    response = co.classify(
        examples=examples,
        inputs=[input_text],
    )

    print(response)

    # gets the prediction of the first classification object in response list
    # NOTE: only one object in list anyways
    return response[0].prediction
