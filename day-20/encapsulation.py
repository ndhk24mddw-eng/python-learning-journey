class Student:
    def __init__(self,name,marks):
        self.__marks = marks
        self.__name = name


    def display(self):
        print('marks of the student is :',self.__marks)
        print('name of the student is :',self.__name)


        #get method
    def get_marks(self):
        return self.__marks   


        #set method
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks = marks
        else:
            print("invalid marks :")    


student1 = Student('ronak',85)

print(student1.get_marks())

student1.set_marks(95)

print(student1.get_marks())
student1.display()       
