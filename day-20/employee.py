class Employee:
    company = "techcrop"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)

    def increase_salary(self, amount):
        self.salary += amount


employee1 = Employee("Ronak Choupal", 100000000000)

employee1.increase_salary(10000)

employee1.display()
Employee.company= "google"
print(employee1.company)