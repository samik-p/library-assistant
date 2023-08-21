from sr import *
from ai import *

# text colors (ANSI)
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

if __name__ == "__main__":
    input = speech_to_text()
    output = get_response(input)

    print(GREEN + "USER INPUT: " + RESET, end="")
    print(input)

    print(BLUE + "RESPONSE: " + RESET, end="")
    print(output)
