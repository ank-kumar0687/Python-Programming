# Write a program to read a file which contains only numbers. Display total 
# of all numbers with maximum and minimum number.

with open("numbers.txt", "r") as file:
    
    data = file.read().split()

    
    numbers = [int(num) for num in data]


total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)


print("Numbers:", numbers)
print("Total:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)