#method overriding
#a child can provide its own version
#  of a method inherited from the parent

class vehicle:
    def start(self):
        print("ypur vehicle is started ;")
class car(vehicle):
    def start(self):
        print("car engine started :")        
car1 = car()
car1.start()