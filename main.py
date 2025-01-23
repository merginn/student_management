import student_operations
import file_handler

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_operations.add_student()
        elif choice == "2":
            student_operations.read_students()
        elif choice == "3":
            student_operations.update_student()
        elif choice == "4":
            student_operations.delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()