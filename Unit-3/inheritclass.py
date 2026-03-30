class Student:

    def __init__(self):
        self.rollno = 101
        self.name = "Ankit"
        self.gender = "Male"
        self.age = 20

    def showStudent(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)


class Course(Student):   

    def __init__(self):
        super().__init__()   
        self.coursename = "Python"
        self.duration = "3 Months"
        self.fee = 5000

    def showCourse(self):
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)



c = Course()


c.showStudent()
c.showCourse()