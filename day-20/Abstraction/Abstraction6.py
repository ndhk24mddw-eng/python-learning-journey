from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def area(self):
        print("Circle area")

    def perimeter(self):
        print("Circle perimeter")


class Square(Shape):

    def area(self):
        print("Square area")
circle = Circle()
square = Square()
