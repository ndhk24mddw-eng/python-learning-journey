class BankAccount:
    bank_name = "SBI"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    # instance method
    def display(self):
        print("name of the account holder :",self.name)
        print("balnce :",self.balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount   
        else:
            print("you bank aaount have not enough balance:")     

    #class method
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name

    # static method
    @staticmethod
    def is_valid_amount(amount):
        return amount>0

holder1 = BankAccount("Ronak",500000)  
holder1.display()  
holder1.deposit(2)
holder1.display()  
holder1.change_bank_name ("indian bank:")
print(holder1.bank_name)
print(holder1.is_valid_amount(5000) )
holder1.withdraw(2)
holder1.display()  


