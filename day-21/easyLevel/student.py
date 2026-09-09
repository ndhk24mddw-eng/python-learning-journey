class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('Name :',self.name)
        print('Marks :',self.marks)
obj1 = Student('Ronak',100)
obj2 = Student('Shiva',100)
obj2.display()
obj1.display()