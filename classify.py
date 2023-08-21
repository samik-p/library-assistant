import os

import cohere
from cohere.responses.classify import Example
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_CLIENT"))

examples = [
    Example("Is Percy Jackson and the Lightning Thief available?", "See librarian"),
    Example("Can I check Gone with the Wind out?", "See librarian"),
    Example("I'm looking for some books about Australia.", "See librarian"),
    Example("What books can help me learn more about dinosaurs?", "See librarian"),
    Example("Are there any library programs happening today?", "See librarian"),
    Example("I need help checking into a computer.", "See librarian"),
    Example("What are the library's hours today?", "Answer"),
    Example("Can teens get volunteer hours here?", "Answer"),
    Example("Where in the library can I find the children's books?", "Answer"),
    Example("Is food allowed at the library?", "Answer"),
    Example("Are masks required to be worn at the library?", "Answer"),
    Example("Hello", "Conversation"),
    Example("Goodbye", "Conversation"),
    Example("How are you doing?", "Conversation"),
    Example("Who are you?", "Conversation"),
]

# sample
inputs = [
    "Is Magic Tree House #39 available at this library?",
    "How long until the library closes?",
]


def classify_input(input_text):
    response = co.classify(
        examples=examples,
        inputs=[input_text],
    )

    return response[0].prediction


# print(classify_input(inputs[0]))
