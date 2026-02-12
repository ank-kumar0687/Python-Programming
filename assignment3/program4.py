p = int(input("Enter Principal amount: "))
t = int(input("Enter Time (in years): "))


def calculate_simple_interest(principal, time, rate=5):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


interest = calculate_simple_interest(p, t)

print("Simple Interest (at 5% rate) =", i
