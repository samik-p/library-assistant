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
        input = speech_to_text()

        if "quit" in input:
            break

        output = get_response(input)

        print(GREEN + "USER INPUT: " + RESET, end="")
        print(input)

        print(BLUE + "RESPONSE: " + RESET, end="")
        print(output)

    print(GREEN + "You have exited the program! Have a nice day :)" + RESET)
