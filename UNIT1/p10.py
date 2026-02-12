'''Write a program to create 4 lambda functions which shall accept 2 
numbers and one arithmetic operator. As per arithmetic operator related 
lambda functions shall be invoked.'''

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Division by zero"


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")


if op == '+':
    result = add(num1, num2)

elif op == '-':
    result = sub(num1, num2)

elif op == '*':
    result = mul(num1, num2)

elif op == '/':
    result = div(num1, num2)

else:
    result = "Invalid operator"


print("Result:", result)