# Write a Python program that takes three integers a, b, and c and determines whether they can form a valid triangle.

# A triangle is valid if:

# a + b > c
# a + c > b
# b + c > a


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a+b > c and a+c >b and b+c > a:
    print('valid triangle :')
else:
    print('Invalid triangle :')
