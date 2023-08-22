from sr import *
from ai import *

from langdetect import detect

# text colors (ANSI)
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

if __name__ == "__main__":
    examples = parse_file_for_examples("examples.txt")
    print(YELLOW + "Training data:" + RESET)
    for example in examples:
        print(f"\t{example}")

    user_messages = []
    while True:
        print(RED + "TYPE 'quit' to exit program")
        print(GREEN + "USER: " + RESET, end="")

        # wait for user input
        input_text = input()  # speech_to_text()
        # print(input_text)   # uncomment if speech_to_text() is used

        # check for whether user quit or not
        if "quit" in input_text:
            break
    
        # detect language of input
        input_lang = detect(input_text)
        

        # append to our conversation
        user_messages.append({"role": "user", "content": f"{input_text}"})
        
        # process input and get response from our AI
        output = get_response(input_text, examples)

        # depending on response, print
        print(BLUE + "RESPONSE: " + RESET, end="")
        if output == "Calling a librarian to help you.":
            print(YELLOW + output + RESET)

            answer = input("Enter an answer: ")
            print(
                BLUE
                + "LIBRARIAN: "
                + RESET
                + process_librarian_response(answer, input_text)
            )
        else:
            print(output)

    print(GREEN + "You have exited the program! Have a nice day :)" + RESET)

    print(RED + "RECEIPT:" + RESET)
    for message in user_messages:
        print(message)
