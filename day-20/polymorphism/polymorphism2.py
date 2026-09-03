# DUCK TYPING
# PYHTON CARE ABOUT WHAT AN OBJECTS CAN DO
# RATHER THAN WHAT CLASS IT BELONGS TO
# A
class Dog:
    def sound(self):
        print('dog barks')
class Cat:
    def sound(self):
        print('mewo')
class Car:
    def sound(self):
        print('horn')
objects = [Dog(),Cat(),Car()]

for obj in objects:
    obj.sound()