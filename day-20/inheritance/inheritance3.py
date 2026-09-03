# chile can have its own attributes
class vehicle:
    def __init__(self,brand):
        self.brand = brand

class car(vehicle):
    def __init__(self,company,brand,model):
        self.company = company
        self.brand = brand
        self.model = model
car1 = car("Toyota","camry")


        