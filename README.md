# Assignment5_python
Python Data Structures Assignment
This repository contains solutions for Module 6: Data Structures and Strings in Python programming assignments.

Contents
This repository includes two Python programs demonstrating dictionary operations and list manipulation:

Task 1: Dictionary of Student Marks - A program that uses dictionaries to store and retrieve student marks.
Task 2: List Slicing Operations - A program that demonstrates list creation, slicing, and reversing.
Task 1: Create a Dictionary of Student Marks
Problem Statement
Write a Python program that:

Creates a dictionary where student names are keys and their marks are values.
Asks the user to input a student's name.
Retrieves and displays the corresponding marks.
If the student's name is not found, displays an appropriate message.
Solution
Copydef student_marks_dictionary():
    # Step 1: Create a dictionary of student names and their marks
    students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 95,
        "Ethan": 88
    }
    
    # Step 2: Ask the user to input a student's name
    student_name = input("Enter the student's name: ")
    
    # Step 3 & 4: Retrieve and display marks, or show message if not found
    if student_name in students:
        print(f"{student_name}'s marks: {students[student_name]}")
    else:
        print("Student not found.")

# Run the function
student_marks_dictionary()
Expected Output
When student exists:

Enter the student's name: Alice
Alice's marks: 85
When student doesn't exist:

Enter the student's name: John
Student not found.
Task 2: Demonstrate List Slicing
Problem Statement
Write a Python program that:

Creates a list of numbers from 1 to 10.
Extracts the first five elements from the list.
Reverses these extracted elements.
Prints both the extracted list and the reversed list.
Solution
Copydef demonstrate_list_slicing():
    # Step 1: Create a list of numbers from 1 to 10
    original_list = list(range(1, 11))
    print(f"Original list: {original_list}")
    
    # Step 2: Extract the first five elements from the list
    extracted_elements = original_list[:5]
    print(f"Extracted first five elements: {extracted_elements}")
    
    # Step 3: Reverse the extracted elements
    reversed_extracted = extracted_elements[::-1]
    print(f"Reversed extracted elements: {reversed_extracted}")

# Run the function
demonstrate_list_slicing()
Expected Output
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
How to Run
Clone this repository to your local machine
Run each Python file using Python 3:
python task1_student_marks.py
python task2_list_slicing.py
For Task 1, follow the prompt to enter a student name
Learning Objectives
This assignment demonstrates understanding of:

Dictionary creation and manipulation in Python
Key checking and value retrieval from dictionaries
List creation and operations
List slicing techniques for extraction and reversal
User input handling
Conditional statements for flow control
