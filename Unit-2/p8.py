

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "D"


with open("students.txt", "r") as file:
    print("RollNo  Name   Total  Percentage  Grade")
    print("----------------------------------------")

    for line in file:
        data = line.strip().split(",")

        roll = data[0]
        name = data[1]
        marks = list(map(int, data[2:]))

        total = sum(marks)
        percentage = total / len(marks)

        grade = get_grade(percentage)

        print(f"{roll}     {name}    {total}     {percentage:.2f}%     {grade}")