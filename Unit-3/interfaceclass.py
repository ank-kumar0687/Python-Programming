from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):

    def __init__(self):
        self.length = 10
        self.width = 5

    def area(self):
        print("Area of Rectangle:", self.length * self.width)



r = Rectangle()
r.area()