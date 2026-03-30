class Student:

    def AddStudent(self):
        self.rollno = int(input("Enter Roll Numbe: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")


    def DisplayStudent(self):
        print("\n--- Student Details ---")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:",self.gender)



s1 = Student()

s1.AddStudent()
s1.DisplayStudent()
