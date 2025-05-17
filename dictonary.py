def student_marks():
    marks_dict = {"Alice": 85, "Bob": 90, "Charlie": 78}

    student_name = input("Enter the student's name: ")

    if student_name in marks_dict:
        print(f"{student_name}'s marks: {marks_dict[student_name]}")
    else:
        print("Student not found.")

student_marks()
