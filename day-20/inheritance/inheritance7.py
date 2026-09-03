# child constructor + super().
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog1 = Dog("Tommy", "German Shepherd")

print(dog1.name)
print(dog1.breed)
#So super() basically allows the child class to access the parent class implementation.