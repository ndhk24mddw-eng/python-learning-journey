# data = (10, 15, 20, 25, 30, 35, 40, 45)

# Create a new tuple containing only the even numbers.

data = (10,15,20,25,30,40,45)
l = []
for i in data:
    if i%2 == 0:
        l.append(i)
l = tuple(l)        
print(l)