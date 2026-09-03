class vehicle:
    def start(self):
        print('vehicle is start:')
class car(vehicle):
    def drive(self):
        print('car is driving :')
class sport(car):
    def race(self):
        print('car is racing')


car1 = sport()
car1.start()
car1.drive()
car1.race()