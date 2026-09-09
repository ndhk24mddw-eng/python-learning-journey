#Multiple Abstract Methods + Partial Implementation.

# An abstract class can contain multiple abstract methods,
#  and a child class 
# must implement all of them before it can be instantiated.

from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):

    def area(self):
        return 10 * 10


class Circle(Shape):
    def area(self):
        return 3.14*5*5
    def perimeter(self):
        return 2*3.14*5


circle = Circle()
square = Square()