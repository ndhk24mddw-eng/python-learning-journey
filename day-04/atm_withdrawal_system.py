# Condition — Hard Problem 2: ATM Withdrawal System

# Create a program that simulates an ATM withdrawal.

# Take:

# Account balance
# Withdrawal amount

# Rules:

# Withdrawal amount must be greater than 0.
# Withdrawal amount must be a multiple of 100.
# Withdrawal amount cannot exceed the account balance.
# If balance after withdrawal becomes less than 500, reject the transaction.
# If all conditions are satisfied, perform the withdrawal and print the remaining balance.

# Example:

# Balance: ₹10000
# Withdrawal: ₹2500


# Withdrawal successful
# Remaining balance: ₹7500

# Example:

# Balance: ₹3000
# Withdrawal: ₹2600


# Transaction rejected
# Minimum balance of ₹500 must be maintained

# You should carefully decide the order of your conditions.

balance = int(input("Enter your balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")

elif withdrawal_amount % 100 != 0:
    print("Withdrawal amount must be a multiple of 100")

elif withdrawal_amount > balance:
    print("Insufficient balance")

elif balance - withdrawal_amount < 500:
    print("Transaction rejected")
    print("Minimum balance of ₹500 must be maintained")

else:
    remaining_balance = balance - withdrawal_amount
    print("Withdrawal successful")
    print("Remaining balance:", remaining_balance)