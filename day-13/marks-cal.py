# Write a function:

# calculate_total(marks)

# The function receives a tuple of marks:

# marks = (85, 72, 91, 65, 88)

# Your function should:

# Calculate the total marks.
# Calculate the percentage.
# Return both values.
# Don't use sum() — calculate the total using a for loop.

# Expected:

# Total: 401
# Percentage: 80.2

def calculate_total(marks):
    marks = list(marks)
    total = 0
    count = 0
    for i in marks:
        total+=i
        count+=1
    percentage = (total / (count * 100)) * 100
    return total,percentage
marks = (85, 72, 91, 65, 88)

total, percentage = calculate_total(marks)

print("Total:", total)
print("Percentage:", percentage)    