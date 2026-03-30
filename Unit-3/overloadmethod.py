
class Number:

    def __init__(self, value):
        self.value = value

    
    def __add__(self, other):
        return self.value + other.value

    
    def __sub__(self, other):
        return self.value - other.value



n1 = Number(10)
n2 = Number(5)


print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)