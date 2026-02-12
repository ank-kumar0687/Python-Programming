# Write a program to create a function which accepts 2 numbers and one 
# arithmetic operator. Return the answer accordingly.




def calculate(a, b, operator):
    
    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    elif operator == '*':
        return a * b

    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    else:
        return "Invalid operator"



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")


result = calculate(num1, num2, op)
print("Result:", result)