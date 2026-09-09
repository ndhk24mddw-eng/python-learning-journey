from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print('pay through UPI:')
class Card(Payment):
    def pay(self):
        print('payment thorough card')
class Cash(Payment):
   
        pass
methods = [UPI(),Card()]
for method in methods:
    method.pay()