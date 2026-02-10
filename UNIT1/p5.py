#Write a program to enter 10 numbers and display largest odd number
#from the entered number.



largest_odd = None

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    
    if num % 2 != 0:   # check odd
        if largest_odd is None or num > largest_odd:
            largest_odd = num


if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number entered")