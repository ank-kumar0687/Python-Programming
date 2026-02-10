#Write a program to enter marks of 4 subjects and display result (result
#shall include total, percentage and grade)


physics = int(input("Enter marks of subject 1: "))
chemistry = int(input("Enter marks of subject 2: "))
math = int(input("Enter marks of subject 3: "))
biology = int(input("Enter marks of subject 4: "))


total = physics + chemistry + math + biology
percentage = (total / 400) * 100


if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 45:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"


print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)