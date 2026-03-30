class Student:

    def __init__(self):
        self.name = "Ankit"
        self.inner = self.Inner()   

    def ankit(self):
        print("Hii I am from the outer class")

    class Inner:   
        def innerShow(self):
            print("Hii I am from the inner class")



s = Student()
s.ankit()
s.inner.innerShow()
