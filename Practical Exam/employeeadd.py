import os

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}"

class ManagementSystem:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = input("Enter Salary: ")
        
        emp = Employee(emp_id, name, dept, salary)
        
        with open(self.filename, "a") as f:
            f.write(str(emp) + "\n")
        print("Employee added successfully!")

    def view_all(self):
        if not os.path.exists(self.filename):
            print("No records found.")
            return
        
        print("\n--- Employee Records ---")
        with open(self.filename, "r") as f:
            for line in f:
                emp_data = line.strip().split(",")
                print(f"ID: {emp_data[0]} | Name: {emp_data[1]} | Dept: {emp_data[2]} | Salary: {emp_data[3]}")

    def search_employee(self):
        search_id = input("Enter Employee ID to search: ")
        found = False
        with open(self.filename, "r") as f:
            for line in f:
                if line.startswith(search_id + ","):
                    print("Record Found:", line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")

    def delete_employee(self):
        search_id = input("Enter Employee ID to delete: ")
        lines = []
        found = False
        
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                lines = f.readlines()
            
            with open(self.filename, "w") as f:
                for line in lines:
                    if not line.startswith(search_id + ","):
                        f.write(line)
                    else:
                        found = True
            
            if found:
                print("Record deleted successfully.")
            else:
                print("ID not found.")


def main():
    sys = ManagementSystem()
    while True:
        print("\n1. Add 2. View All 3. Search 4. Delete 5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1': sys.add_employee()
        elif choice == '2': sys.view_all()
        elif choice == '3': sys.search_employee()
        elif choice == '4': sys.delete_employee()
        elif choice == '5': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
