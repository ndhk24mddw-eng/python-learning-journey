# abstract methods + super()
from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,amount):
        self.amount = amount
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def __init__(self,amount,upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    def pay(self):
        print('paying',self.amount,'using upi')



upi = UPI("500", "ronak@upi")
upi.pay()
print(upi.upi_id)


# super() means:

# Access the parent implementation
#  according to Python's inheritance/MRO.