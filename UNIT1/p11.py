# Write a program to create function which shall accept any number of 
# arguments and display total of all the numbers given as argument.



def total_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    print("Total of all numbers:", total)


total_numbers(10, 20, 30, 40)