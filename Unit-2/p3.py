import logging


logging.basicConfig(filename="error.txt", level=logging.ERROR)

try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    c = a / b
    print("Reslut:",c)


except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
    logging.error(e)


print("Program Ended")
    
