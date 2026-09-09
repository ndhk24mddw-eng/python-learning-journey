from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):

    def sound(self):
        print("Bark")
dog = Dog()

dog.sound()
dog.sleep()