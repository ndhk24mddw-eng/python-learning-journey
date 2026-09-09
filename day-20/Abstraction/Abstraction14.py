# abstract method + super()
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def Company(self):
        return "Sage"


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(
            "My name is", self.name,
            "I work at", self.Company(),
            "My salary is", self.salary,
            "I use", self.language
        )


obj = Developer("Ronak", 3000000000, "Python")

obj.work()