class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return (self.length * self.width)
    def perimeter(self):
        return 2* (self.length + self.width)
    def display(self):
        print(self.area())
        print(self.perimeter())
rectangle = Rectangle(10, 5)
rectangle.display()