# Tuple — Medium Logical Question 4/15

# Given:

# data = (
#     ("Python", 85),
#     ("DSA", 72),
#     ("DBMS", 91),
#     ("SEPM", 65),
#     ("CN", 88)
# )

# Find the subject with the highest marks.

# Expected output:

# Highest Subject: DBMS
# Highest Marks: 91

data = (
    ("Python", 85),
    ("DSA", 72),
    ("DBMS", 91),
    ("SEPM", 65),
    ("CN", 88)
)
highest_marks = 0
highest_subject = ""

for sub, marks in data:
    if marks > highest_marks:
        highest_marks = marks
        highest_subject = sub
       

print("Highest Subject:", highest_subject)
print("Highest Marks:", highest_marks)