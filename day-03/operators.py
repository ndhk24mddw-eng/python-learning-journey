# Write a program that takes an integer from the user and prints:

# Whether the number is even or odd.
# Whether the number is positive, negative, or zero.

# Use comparison and arithmetic operators.

num = int(input("Enter the integer :"))


if num%2 == 0:
   print("number is even :",num)
else:
    print ('number is odd :',num)   


if num >0:
    print('num is positive :',num)
if num == 0:
    print("num is zero :")
if num<0:
    print('Num is negative :',num)
   
