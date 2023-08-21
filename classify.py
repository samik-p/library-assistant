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


# examples = [
#     Example("Is Percy Jackson and the Lightning Thief available?", "See librarian"),
#     Example("Can I check Gone with the Wind out?", "See librarian"),
#     Example("I'm looking for some books about Australia.", "See librarian"),
#     Example("What books can help me learn more about dinosaurs?", "See librarian"),
#     Example("Are there any library programs happening today?", "See librarian"),
#     Example("Is Magic Tree House #39 available at this library?", "See librarian"),
#     Example("I need help checking into a computer.", "See librarian"),
#     Example("What are the library's hours today?", "Answer directly"),
#     Example("Can teens get volunteer hours here?", "Answer directly"),
#     Example("Where in the library can I find the children's books?", "Answer directly"),
#     Example("Is food allowed at the library?", "Answer directly"),
#     Example("Are masks required to be worn at the library?", "Answer directly"),
#     Example("How long until the library closes?", "Answer directly"),
#     Example("Hello", "Conversation"),
#     Example("Goodbye", "Conversation"),
#     Example("How are you doing?", "Conversation"),
#     Example("Who are you?", "Conversation"),
# ]
