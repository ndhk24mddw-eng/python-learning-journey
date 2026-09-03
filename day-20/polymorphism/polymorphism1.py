
class Animal:
    def sound(self):
        print('animal is saying some thing :')

class Dog(Animal):
    def sound(self):
        print('dog is barking for food :')

class Cat(Animal):
    def sound(self):
        print('mewo')

animals = [Dog(),Cat()]        
for animal in animals:
    animal.sound()