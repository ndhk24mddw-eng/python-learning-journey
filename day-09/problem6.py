# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:

# [34, 67, 89]

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
l = []

for i in range(0,len(num1)):
    for j in range(0,len(num2)):
        if num1[i] == num2[j]:
           l.append(num1[i])
print(sorted(l))