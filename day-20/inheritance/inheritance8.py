# reat. Next concept: Method Overriding.

# Method overriding happens when the child class provides its own
#  version of a method that already exists in the parent class.
class animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print('animal make sound :')    
    def eat(self):
        print('animals are eating')
class Dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        print(self.name,'dog is barking')  
    def eat(self):
        print(self.name,'dog is eating :') 
        super().eat()  
dog1 = Dog('tommy','germanshephared')       
dog1.sound()
dog1.eat()