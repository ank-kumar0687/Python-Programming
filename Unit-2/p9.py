
students = {}


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!\n")


def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print("Found:", students[roll])
    else:
        print("Student not found!")
    print()


def list_students():
    if not students:
        print("No students available!\n")
        return
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['name']}, Marks: {details['marks']}")
    print()


def update_student():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student updated successfully!")
    else:
        print("Student not found!")
    print()


def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")
    print()

while True:
    print("---- Student Menu ----")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter your choice: ")

    if choice == 'a':
        add_student()
    elif choice == 'b':
        search_student()
    elif choice == 'c':
        list_students()
    elif choice == 'd':
        update_student()
    elif choice == 'e':
        delete_student()
    elif choice == 'f':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")