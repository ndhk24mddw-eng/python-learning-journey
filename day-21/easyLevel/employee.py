class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def increase_salary(self,percent):
        self.salary = self.salary+(self.salary*percent*0.001)
        return self.salary
    def display(self):

        print(self.name,':',self.salary)
employee = Employee("Ronak", 50000)
employee.increase_salary(10)
employee.display()
