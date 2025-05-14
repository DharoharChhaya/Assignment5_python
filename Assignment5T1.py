def student_marks_dictionary():
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
