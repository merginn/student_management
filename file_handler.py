import json

FILE_NAME = "students.txt"

def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_file(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_to_file(student):
    students = read_file()
    students.append(student)
    write_file(students)