# Given:

# data = (10, 20, 30, 40, 50, 60)

# Take an integer k from the user 
# and rotate the tuple to the right by k positions.

data = (10, 20, 30, 40, 50, 60)

k = int(input('enter the integer : '))
k = k % len(data)
data = list(data)
num1 =data[-k:]
num2 = data[:-k]

result = tuple(num1+num2)
print(result)

