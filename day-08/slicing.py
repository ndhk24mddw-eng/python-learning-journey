# String Slicing — Question 1/2

# Take a string from the user and print:

# First 5 characters
# Last 5 characters
# Characters from index 2 to 6
# Every second character
# The complete string in reverse

# Example:

# Enter string: PythonProgramming

# First 5: Pytho
# Last 5: mming
# Index 2 to 6: thonP
# Every second: PtoPormn
# Reverse: gnimmargorPnohtyP

# Use slicing only for these operations.

# Write the code yourself and send it.

s = input("enter your sentence :")
print(s[0:5])

print(s[2:6])
print(s[0::2])
print(s[::-1])
