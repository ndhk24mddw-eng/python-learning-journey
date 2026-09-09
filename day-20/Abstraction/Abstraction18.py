from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(amount, 'pay using upi')


class Card(Payment):

    def pay(self, amount):
        print(amount, 'pay using card')


class NetBanking(Payment):

    def pay(self, amount):
        print(amount, 'pay by NetBanking')


class Cash(Payment):

    def pay(self, amount):
        print(amount, 'paid using Cash')


def process_payment(payment):
    payment.pay(5000)


process_payment(UPI())
process_payment(NetBanking())
process_payment(Card())
process_payment(Cash())