# Take two integers as input and calculate:

# Sum
# Difference
# Product
# Division
# Floor division
# Remainder

num1 = int(input('Enter the integer :'))
num2 = int(input('Enter the integer :'))

op = input('Enter the operator :')
if op == '+':
    print('sum of  num1 and num 2 :',num1 + num2)
elif op == '*':
    print(' product :',num1*num2)
elif op == '/':
    print('div :',num1/num2)
elif op == '//':
    print('integer div :',num1//num2)
elif op == '%':
    print('remainder :',num1%num2)
elif op == '-':
    print('substract :',num1-num2)
else:
    print('Invalid operator :')




