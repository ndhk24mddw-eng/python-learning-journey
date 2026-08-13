# Write a program which can remove a particular character from a string.
s = input("input the string :")
c = input("input the character which you want remove :")
result = ''
for i in s:
 if i != c:
  result += i

print (result)

