class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Robot:
    def speak(self):
        print("Beep")


def make_speak(objects):
    for obj in objects:
        obj.speak()


items = [Dog(), Robot(), Cat(), Dog()]

make_speak(items)