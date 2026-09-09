from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    def company(self):
            print('Working at TechCorp')

        
class Developer(Employee):
    def work(self):
        print('developer is developing')
class Manager(Employee):
    def work(self):
        print('Manager is managing')
    

developer = Developer()
manager = Manager()    

developer.work()
developer.company()

manager.work()
manager.company()