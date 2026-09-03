class  Dog:
    def sound(self):
        print(' dog is barking :')
class  Cat:
    def sound(self):
        print(' mewo')
class Car:
    def sound(self):
        print(' horn :')   
dog = Dog()
cat = Cat()
car = Car()     

def make_sound(animal):
    animal.sound()

make_sound(dog)
make_sound(cat)
make_sound(car)

