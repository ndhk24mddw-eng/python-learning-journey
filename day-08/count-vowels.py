# Write a Python program that takes a string 
# and counts how many vowels and consonants it contains.
string = input('enter the string :')
vowel_count = 0
consonant_count = 0
for i in string:
    if i.isalpha():
        if i in  "aeiouAEIOU":
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count) 
       



   
