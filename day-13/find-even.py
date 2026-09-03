def find_even(numbers):
    numbers = list(numbers)
    result = []
    for i in numbers:
        if i%2 == 0:
            result.append(i)
    return result

numbers = (10, 15, 22, 31, 40, 55, 60, 73)

even = find_even(numbers)
print(even)