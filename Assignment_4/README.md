# Tutedude Assignment-4:
## Task 1: Read a File and Handle Errors and 
1. Opens and reads a text file named sample.txt.</br>
  with open("sample.txt", "r") as file: </br>

1. Prints its content line by line and </br>

 for index, line in enumerate(file, start=1):</br>
            print(f"Line {index}: {line.strip()}")
 </br>
2.Handles errors gracefully if the file does not exist.</br>
try:</br>

except FileNotFoundError:</br>
    print("Error: The file 'sample.txt' was not found.")</br>


## Task 2: Write and Append Data to a File</br>
 
1.   Takes user input and writes it to a file named output.txt. using w </br>
with open("output.txt", "w") as file:.</br>
    file.write(inp + "\n").</br>
2.   Appends additional data to the same file. using a</br>
with open("output.txt", "a") as file:.</br>
    file.write(in_extra + "\n").</br>

3.   Reads and displays the final content of the file.</br>
with open("output.txt", "r") as file:.</br>
    for index, line in enumerate(file, start=1):.</br>
        print(f"Line {index}: {line.strip()}") .</br>




