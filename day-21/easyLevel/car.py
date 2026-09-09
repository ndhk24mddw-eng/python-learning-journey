class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print('Model of the car is :',self.model)
        print('Brand of the car is :',self.brand)
        print('Price  of the car is :',self.price)
obj1 = Car('Toyota','Fortuner',5000000)
obj1.display()
car2 = Car('BMW','x5',9500000)
car2.price = 10000000
car2.display()
car3 = Car('Thar','rock',6000000)
car3.display()