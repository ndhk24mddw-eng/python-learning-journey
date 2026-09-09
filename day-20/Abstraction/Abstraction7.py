from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def  start(self):
        print('car is start')
    def stop(self):
        print('car will be stop')
    def fuel_type(self):
        print('petrol')

class Bike(Vehicle):
    def start(self):
        print("bike start")
    def stop(self):
        print('bike stop')
car = Car()
bike = Bike()

# If a child implements ALL inherited abstract methods 
# → it becomes concrete → its object can be created.

# If even ONE abstract method is not implemented → 
# it remains abstract → its object cannot be created.
