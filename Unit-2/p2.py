# Write a program to execute user defined exception in python.


class MyError(Exception):
    pass


try:
    num = int(input("Enter a number greater than 10: "))
    
    if num <= 10:
        raise MyError("Number is too small!")
    
    print("You entered:", num)

except MyError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a number.")

print("Program Ended")