import os

import requests
from bs4 import BeautifulSoup


# text colors (ANSI)
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"


def get_filenames_in_folder(folder_path):
    try:
        filenames = os.listdir(folder_path)
        return filenames
    except FileNotFoundError:
        print(RED + f"Folder '{folder_path}' not found." + RESET)
        return []
    except Exception as e:
        print(RED + f"An error occurred: {e}" + RESET)
        return []


def remove_files_with_numbered_names(folder_path):
    try:
        filenames = os.listdir(folder_path)
        for filename in filenames:
            if filename[0].isdigit():  # Check if filename starts with a digit
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                print(GREEN + f"Removed file: {filename}" + RESET)
    except FileNotFoundError:
        print(RED + f"Folder '{folder_path}' not found." + RESET)
    except Exception as e:
        print(RED + f"An error occurred: {e}" + RESET)


def get_links_from_pages_in_file(fname):
    filepath = f"results/{fname}.txt"
    try:
        with open(filepath, "r") as file:
            line_number = 1
            for url in file:
                url = url.strip()  # Remove leading/trailing whitespace
                # Process the line here
                print(f"{line_number}: ", end="")
                links = get_links_from_page(url)

                if links:
                    filename = f"{line_number}-file"

                    put_links_in_file(filename, links)

                else:
                    print(YELLOW + "No links found." + RESET)

                line_number += 1

    except FileNotFoundError:
        print(RED + f"File '{fname}' not found in /results/" + RESET)
    except Exception as e:
        print(RED + f"An error occurred: {e}" + RESET)


# def get_links_from_page(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, "html.parser")
#         write_string_to_file(soup.prettify(), "content.html")
#         links = soup.find_all("a", href=True)
#         return [link["href"] for link in links]
#     else:
#         print(RED + f"Failed to fetch the page. ", end="")
#         return []


def get_links_from_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        write_string_to_file(soup.prettify(), "content.html")
        links = soup.find_all("a", href=True)
        return [link["href"] for link in links]
    else:
        print(RED + f"Failed to fetch the page. ", end="")
        return []


def write_string_to_file(input_string, filename):
    with open(filename, "w") as file:
        file.write(input_string)


def put_links_in_file(fname, links):
    if links:
        output_filename = f"results/{fname}.txt"

        result_string = ""

        num_links = 0
        for link in links:
            if "http" in link and "polic" in link:
                result_string += f"{link}\n"
                num_links += 1

        if num_links != 0:
            write_string_to_file(result_string, output_filename)
            print(
                GREEN
                + f"{num_links} links have been written to the following file: '{output_filename}'"
                + RESET
            )
        else:
            print(YELLOW + "No links found." + RESET)
    else:
        print(YELLOW + "No links found." + RESET)


if __name__ == "__main__":
    running = True
    while running:
        files = get_filenames_in_folder("results/")
        files.sort()
        print("\nFiles:")
        print(BLUE + ".\n" + RESET + "└── " + BLUE + "results" + RESET)
        for file in files[:-1]:
            print("    ├── " + GREEN + f"{file}" + RESET)
        print("    └── " + GREEN + f"{files[-1]}" + RESET)

        print(
            BLUE
            + "TYPE '~' to delete generated number files.\nTYPE '@' to exit program\n"
            + RESET
        )
        fname = input("Enter the name of a file: ")

        if fname == "~":
            remove_files_with_numbered_names("results/")
        elif fname == "@":
            running = False
        else:
            get_links_from_pages_in_file(fname)

        # break
