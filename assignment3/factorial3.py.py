
num = int(input("Enter a number: "))

def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial (Iterative) =", factorial_iterative(num))
