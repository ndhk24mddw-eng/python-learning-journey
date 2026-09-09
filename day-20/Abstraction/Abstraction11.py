from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")

upi = UPI()
card = Card()

upi.pay(500)
card.pay(1000)


# The important point is 
# that the parent decides what operation must exist, 
# but the child decides how that operation works.

# This is abstraction + polymorphism working together.