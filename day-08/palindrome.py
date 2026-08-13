# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('string :')
flag = True
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
      flag = False
      break
    
       
if flag:
    print("String is palindrome :")    
else:
    print ("not palindrone :")    

