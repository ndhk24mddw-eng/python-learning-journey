class vehicle:
    def start(self):
        print("vehicle is start :")
    def stop(self):
        print("vehicle is stop")
class car(vehicle):
    def honk(self):
        print("beep beep :")
               
car1 = car()
car1.start()
car1.honk()