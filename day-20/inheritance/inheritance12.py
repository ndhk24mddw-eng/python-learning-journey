# Multiple Inheritance

# Multiple inheritance means 
# one child class inherits from two or more parent classes.
class Father:
    def skills(self):
        print("Father: Driving")


class Mother:
    def cooking(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def play(self):
        print("Child: Playing")


child1 = Child()

child1.skills()
child1.cooking()
child1.play()