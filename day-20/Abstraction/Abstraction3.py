from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Cash(Payment):
    def pay(self,amount):
        print(amount,'amount is paid in cash')
class Card(Payment):
    def pay(self,amount):
        print(amount,'amount is paid by card :')
class UPI(Payment):
    def pay(self,amount):
        print(amount,'amount is paid through UPI')
class NetBanking(Payment):
    def pay(self,amount):
        print(amount,'amount is paid through NetBanking')

card = Card()
cash = Cash()
netbanking = NetBanking()
upi = UPI()



card.pay(2000)
cash.pay(400)
upi.pay(3443)
netbanking.pay(5858)