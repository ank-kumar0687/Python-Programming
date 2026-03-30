
from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def show(self):
        pass



class Demo(Student):

    def show(self):
        print("This is abstract method implementation")



d = Demo()
d.show()