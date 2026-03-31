import matplotlib.pyplot as plt


n = int(input("Enter number of courses: "))

courses = []
students = []


for i in range(n):
    course = input(f"Enter name of course {i+1}: ")
    count = int(input(f"Enter number of students in {course}: "))
    
    courses.append(course)
    students.append(count)


max_index = students.index(max(students))


explode = [0] * n
explode[max_index] = 0.2   


plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')

plt.title("Students in Different Courses")


plt.show()
