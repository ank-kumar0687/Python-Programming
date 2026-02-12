num = int(input("Enter a number: "))

def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:   
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Factorial (Recursive) =", factorial_recursive(num))
