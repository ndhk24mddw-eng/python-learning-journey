class student:
    def __init__(self,marks):
        self.__marks = marks

    #get method
    def marks(self):
        return self.marks 

student1 = Student(85)
print(student1.marks)
