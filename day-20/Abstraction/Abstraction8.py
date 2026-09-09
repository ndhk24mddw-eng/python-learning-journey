from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):

    def start(self):
        print("Car started")
car = Car("Toyota")
print(car.brand)