# Next concept: __init__() with inheritance

class animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('the ',self.name,'eating')    
    def sleep(self):
        print('the',self.name,'is sleeping ')  
class dog(animal):
    pass
dog1 = dog('shivam')
dog1.eat() 
dog1.sleep()         