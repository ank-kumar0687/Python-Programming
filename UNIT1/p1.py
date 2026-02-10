# Write a program to input p, r, n and find out interest using simple input
#output statement.


p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
n = int(input("Enter time (in years): "))

si = (p * r * n) / 100


print("Simple Interest is:", si)

