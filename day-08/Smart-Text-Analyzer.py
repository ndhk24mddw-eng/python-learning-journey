# Project 1 — Smart Text Analyzer

# Level: Medium

# Build a program that takes a sentence from the user and analyzes it.

# It should:

# Take a sentence.
# Remove unnecessary spaces from the beginning/end.
# Print:
# Original sentence
# Cleaned sentence
# Number of characters
# First character
# Last character


# Convert the sentence into:
# lowercase
# uppercase
# title case

# Count how many times a character entered by the user occurs.
# Check whether the sentence:
# starts with a character/word entered by the user
# ends with a character/word entered by the user
# Check whether a word entered by the user exists in the sentence.
# Split the sentence into words.
# Join the words using -.

s = input(""" Ente the sentence : """)
sentence = s.strip()
print('number of character present in this sentence is :',len(sentence))
print('first character of the sentence is :',sentence[0])
print('last character of the sentence is :',sentence[-1])
print(sentence.capitalize())
print(sentence.title())
print(sentence.lower())
print(sentence.upper())
print(sentence.swapcase())
print(sentence.count('p'))
print(sentence.find('python'))
print(sentence.startswith('python'))
print(sentence.endswith('python'))
print(sentence.isalnum())
print(sentence.isalpha())
print(sentence.isdigit())
print(sentence.isidentifier())
print(sentence.split())
print("-".join(sentence.split()))
print(sentence.replace('python','c++'))


