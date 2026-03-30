class Student:

    def __init__(self):
        self.rollno = 101
        self.name = "Ankit"

    def showStudent(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)


class Course:

    def __init__(self):
        self.coursename = "Python"
        self.fee = 5000

    def showCourse(self):
        print("Course Name:", self.coursename)
        print("Fee:", self.fee)


class Result(Student, Course):   

    def __init__(self):
        Student.__init__(self)
        Course.__init__(self)
        self.marks = 85

    def showResult(self):
        print("Marks:", self.marks)



r = Result()


r.showStudent()
r.showCourse()
r.showResult()


print("\nMRO of Result Class:")
for cls in Result.mro():
    print(cls)