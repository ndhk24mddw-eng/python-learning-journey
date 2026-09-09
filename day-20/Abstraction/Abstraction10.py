from abc import ABC,abstractmethod
class Employee(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod
    def work(self):
        pass
    def company(self):
        print('sage indore :')
class Developer(Employee):

    def work(self):
        print(self.name,'coding')
developer = Developer("Ronak")
developer.work()
developer.company()