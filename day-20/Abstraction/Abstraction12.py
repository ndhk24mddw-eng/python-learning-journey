from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def calculate(self,a,b):
        pass

class Addition(Calculator):
    def calculate(self,a,b):
         return a+b
class Subtraction(Calculator):
    def calculate(self, a, b):
        return a - b
   
obj = Addition()
result = obj.calculate(10,20)
print(result)
obj = Subtraction()
print(obj.calculate(20, 8))