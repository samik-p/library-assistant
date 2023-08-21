from sr import *
from ai import *

# text colors (ANSI)
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

if __name__ == "__main__":
    while True:
        print(GREEN + "USER: " + RESET, end="")
        # print(input_text)

        input_text = input()  # speech_to_text()

        if "quit" in input_text:
            break

        output = get_response(input_text)

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
