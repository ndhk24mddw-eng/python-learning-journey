from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")


class SportsCar(Car):

    def stop(self):
        print("Sports car stopped")


sports_car = SportsCar()

sports_car.start()
sports_car.stop()