# Tuple — Medium Logical Question 2/15

# Given:

# data = (10, 15, 20, 25, 30, 15, 40, 20, 50)

# Create a new tuple containing only the 
# elements that occur exactly once.

data = (10, 15, 20, 25, 30, 15, 40, 20, 50)
print(data.count(15))
result = []
for i in data:
    if data.count(i) == 1:
        result.append(i)
result = tuple(result)        
print(result)

