# #poly = many
# #morph = forms
# polymorphism means one interface many form
# in programmming the same method can behave defferently depending
# example :
class dog:
    def sound(self):
        print('dog is barking')
class cat:
    def sound(self):
        print('cant meow')

# in this both clas have sound but bheavior different
dog = dog()
cat = cat()

dog.sound()
cat.sound()