#Write a program to input 2 numbers and one arithmetic operator. Perform
#operations as per arithmetic operator which is given as input


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


op = input("Enter operator (+, -, *, /): ")


if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    result = x / y
else:
    print("Invalid operator")
    result = None


if result is not None:
    print("Result is:", result)