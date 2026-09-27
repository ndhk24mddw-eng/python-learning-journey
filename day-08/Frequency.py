# Write a Python program that takes a 
# string and finds the frequency of each character.
string = input('enter a string :')
frequency = {}
for i in string:
    if i.isalpha():
        i = i.lower()
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
print(frequency)
    


       

