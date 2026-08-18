# Problem 2 — Easy

#Write a Python program that takes two numbers from the user and prints:

#Their sum
#Their difference
#Their multiplication
#Their division


s = int(input("Enter the first number: "))
z = int(input("Enter the second number: "))

op = input("Enter the operator: ")

if op == '+':
    print("Sum of s and z:", s + z)

elif op == '-':
    print("Subtraction of s and z:", s - z)

elif op == '*':
    print("Multiplication of s and z:", s * z)

elif op == '/':
    print("Division of s and z:", s / z)

else:
    print("Invalid operator")
