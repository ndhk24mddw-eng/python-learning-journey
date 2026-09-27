# Write a Python program 
# to check whether a given string is a palindrome.
string = input('enter the string :')
string = string.lower()
string = string.replace(" ", "")
rev = string[::-1]
if string == rev:
    print('palindrome')
else:
    print('not plaindrome :')



    

