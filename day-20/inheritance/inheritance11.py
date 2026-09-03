class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

dog1 = Dog()
cat1 = Cat()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()