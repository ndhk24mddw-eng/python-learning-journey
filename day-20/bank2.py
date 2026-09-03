class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

        
    #get method    
    @property    
    def balance(self):
        return self.__balance


    #setter method     
    @balance.setter
    def balance(self,value):
        if value >=0:
            self.__balance= value
        else:
            print("bhai amount dalaoo sahi se :")    
#obj
account1 = BankAccount("ronak choupal :",500000000)
print(account1.balance)
account1.balance = 600000000
print(account1.balance)


