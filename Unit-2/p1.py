# Write a program to display basic exception handling in python.

try:

    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number
    print(f"Result is: {result}")

except ZeroDivisionError:
    
    print("Error: You cannot divide by zero!")

except ValueError:
    
    print("Error: Please enter a valid integer.")

except Exception as e:
    
    print(f"An unexpected error occurred: {e}")

finally:
    
    print("Execution complete.")