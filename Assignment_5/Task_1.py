# Task 1: Create a Dictionary of Student Marks

#Creates a dictionary where student names are keys and their marks are values.
dict_marks={
    "Priya": 96,
    "Ayasha": 86,
    "Meenu": 92,
    "Harshita": 91,
    "Shivani": 89
}
#Asks the user to input a student's name.

inp=input("Enter the student's name :")
# Retrieves and displays the corresponding marks.
#If the student’s name is not found, display an appropriate message.
if inp in dict_marks:
    print("{}'s marks is {}".format(inp,dict_marks[inp]))
else:
    print("Student not Found.")
    


