import cohere
from cohere.responses.classify import Example

co = cohere.Client('puYypsQK320muLPDCwjT4nWOZVfHMdjOa036ShcI')

examples=[
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
]
inputs=[
  "Is Magic Tree House #39 available at this library?",
  "How long until the library closes?",
]

response = co.classify(
  inputs=inputs,
  examples=examples,
)
print(response)