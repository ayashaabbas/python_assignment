# Task 1: Read a File and Handle Errors

# Opens and reads a text file named sample.txt.
# Prints its content line by line.
# Handles errors gracefully if the file does not exist.

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")  #
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
