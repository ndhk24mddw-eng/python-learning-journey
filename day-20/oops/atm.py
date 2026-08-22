# creating class of atm
class ATM:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    # creating obj
    def menu(self):
        user_input = input("""hi how can i help you sir :
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdrawal
        5. any thing else to exit """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdrawal_balance()
        else:
            exit()

    # creating function

    # function for pin
    def create_pin(self):
        user_pin = input('enter your new pin :')
        self.pin = user_pin

        user_balance = int(input('enter your balance :'))
        self.balance = user_balance

        print("your pin is created successfully :")
        self.menu()

    # creating function for change pin
    def change_pin(self):
        old_pin = input('enter your old pin :')

        if old_pin == self.pin:
            new_pin = input('enter your new pin :')
            self.pin = new_pin
        else:
            print('invalid pin :')

        self.menu()

    # creating function for check balance
    def check_balance(self):
        user_pin = input('enter your pin :')

        if user_pin == self.pin:
            print('your balance is :', self.balance)
        else:
            print('invalid pin :')

        self.menu()

    # creating function for withdrawal amount
    def withdrawal_balance(self):
        user_pin = input("enter your pin :")

        if user_pin == self.pin:
            amount = int(input("enter withdrawal amount :"))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdrawal successful balance is ', self.balance)
            else:
                print('invalid amount :')

        else:
            print('invalid password :')

        self.menu()


# creating object
atm = ATM()