class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount<0:
            print('please enter valid amount :')
        else:
            self.balance+=amount
    def display(self):
        print('Balance :',self.balance)
account = BankAccount('Ronak', 5000)
account.deposit(2000)
account.display()