# Given this nested tuple:

# data = (
#     ("Ronak", 85),
#     ("Aman", 72),
#     ("Rahul", 91),
#     ("Priya", 65),
#     ("Neha", 88)
# )

# Each inner tuple contains:

# (name, marks)

# Your task is to create a new tuple
#  containing only students who scored 80 or more.

data = (
    ("Ronak", 85),
    ("Aman", 72),
    ("Rahul", 91),
    ("Priya", 65),
    ("Neha", 88)
)

result = []

for name,marks in data:
    if marks >= 80:
        result.append((name,marks))
result =tuple(result)
print(result)        