# Converts the list into a set to remove duplicates.
# Finds the number of unique elements.
# Checks whether 50 exists.
# Checks whether 100 exists.
# Creates a new set containing only numbers greater than 30.

data = [10, 20, 10, 30, 40, 20, 50, 30, 60, 10]
data = set(data)
s = set()
print(50 in data)
print(100 in data)
for i in data:
    if i>30:
        s.add(i)
print(s)        


print(len(data))
print(data)