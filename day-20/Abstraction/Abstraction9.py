from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand):
        self.band = brand
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def start(self):
        print('start the BMW')

car = Car("Toyota", "Camry")
car.start()
print(car.model)