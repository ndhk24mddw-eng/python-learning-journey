# Python Mini-Project 2 — Personal Expense & Budget Analyzer
expenses= [
  
   ["2026-09-01", "Food", "Lunch", 180, "UPI"],

    ["2026-09-01", "Transport", "Auto", 120, "Cash"],

    ["2026-09-02", "Education", "Python Book", 500, "UPI"],

    ["2026-09-03", "Shopping", "T-Shirt", 800, "Card"],

    ["2026-09-04", "Food", "Dinner", 250, "UPI"]

]


expenses.append(['2027-09-09','Entertainment','movei',3000,'upi'])
expenses.append(['2026-09-06','food','Breakfast',100,'cash'])
expenses.append(['2026-09-06','Transport','bus',50,'UPI'])
expenses.append(['2026-09-06','Education','Note BOok',60,'cash'])
deleted_expense = expenses.pop()
expenses.remove(expenses[0])
for expense in expenses:
    print("Date:", expense[0])
    print("Category:", expense[1])
    print("Description:", expense[2])
    print("Amount:", expense[3])
    print("Payment Method:", expense[4])
print('deleted expense:',deleted_expense)


# # Challenge 1: Print the amount of the first expense.

# print('the amount of the first expense',expenses[0][3])
# # Challenge 2: Print the category of the third expense.
# print('the category of the third expense.',expenses[2][1])


# # Challenge 3: Print the description of the last expense.
# print('the description of the last expense',expenses[4][2])

# # Challenge 4: Print the payment method of the second expense.
# print('the payment method of the second expense',expenses[1][4])

# # Challenge 5: Print the complete fourth expense.
# print(expenses[3])

