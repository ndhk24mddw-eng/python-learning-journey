from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class Cash(Payment):
    def pay(self):
        print('payment through cash')
class UPI(Payment):
    def pay(self):
        print('payment though cash :')
class Card(Payment):
    pass
class NetBanking(Payment):
    def pay(self):
        print ("payment thorugh NetBanking")    

methods = [Cash(),UPI(),NetBanking()]
for method in methods:
    method.pay()