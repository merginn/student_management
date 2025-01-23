import file_handler

def add_student():
    student = {
        "name": input("Enter student name: "),
        "age": input("Enter student age: "),
        "group": input("Enter student group: ")
    }
    file_handler.add_to_file(student)
    print("Student added successfully!")

def read_students():
    students = file_handler.read_file()
    print("\nStudent Records:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Group: {student['group']}")

def update_student():
    students = file_handler.read_file()
    read_students()
    try:
        name = input("Enter the student name to update: ")
        for student in students:
            if student["name"] == name:
                student.update({
                    "name": input("Enter new name: "),
                    "age": input("Enter new age: "),
                    "group": input("Enter new group: ")
                })
                file_handler.write_file(students)
                print("Student updated successfully!")
                return
        print("Student not found.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

def delete_student():
    students = file_handler.read_file()
    read_students()
    try:
        name = input("Enter the student name to delete: ")
        for student in students:
            if student["name"] == name:
                students.remove(student)
                file_handler.write_file(students)
                print("Student deleted successfully!")
                return
        print("Student not found.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
