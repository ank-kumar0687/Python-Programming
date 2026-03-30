class Student:
 

    def  ankit(self, name, marks):
        self.name = name
        self.marks = marks

    
    def display_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

obj = Student()
obj.ankit("Ankit", 456)
obj.display_details()
