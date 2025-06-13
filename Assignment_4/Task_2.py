# Task 2 : Write and Append Data to a File
 
#Takes user input and writes it to a file named output.txt. 
inp= input("Enter text to write to file: ")

with open("output.txt", "w") as file:
    file.write(inp + "\n")

print("Data successfully written to output.txt.")

# Appends additional data to the same file.</br>
in_extra = input("Enter additional text to append : ")

with open("output.txt", "a") as file:
    file.write(in_extra + "\n")

print("data succesfully appended.")

#Reads and displays the final content of the file.</br>
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"Line {index}: {line.strip()}")
