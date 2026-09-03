# Duplicate Compression

# Given:

# data = (
#     10, 10, 20, 20, 20,
#     30, 10, 40, 40, 50,
#     50, 50, 60
# )

# Create a new tuple where consecutive
#  duplicate values are compressed into a single value.
data = (
    10, 10, 20, 20, 20,
    30, 10, 40, 40, 50,
    50, 50, 60
)

data = list(data)
n = len(data)
result = []
for i in range(0,n-1):
    if data[i] != data[i+1]:
        result.append(data[i])
result.append(data[-1]) 
result = tuple(result)       
print(result)           

