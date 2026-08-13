# Write a program to count the number of words in a string without split()

s = input("Enter the string :")
L =[]

temp = ' '
count = 0

for i in s:
    if i != ' ':
        temp = temp + i
    else:
        L.append(temp)    
        temp = ''
print(L)        



