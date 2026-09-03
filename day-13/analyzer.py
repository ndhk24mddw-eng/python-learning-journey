# Find the sum of all even numbers.
# Find the sum of all odd numbers.
# Count how many even numbers there are.
# Count how many odd numbers there are.
# Return all four results.

def analyze_numbers(numbers):
    even_count = 0
    sum_even = 0
    odd_count = 0
    sum_odd = 0
    for i in numbers:
        if i%2 == 0:
            even_count+=1
            sum_even+=i
        else:
            odd_count+=1
            sum_odd+=i
    return sum_even,sum_odd,even_count,odd_count

numbers = (10, 15, 22, 31, 40, 55, 60, 73)

sum_even,sum_odd,even_count,odd_count = analyze_numbers(numbers)

print("sum of even number is :",sum_even)
print("sum of odd number is :",sum_odd)
print("numbers of even  :",even_count)
print("numers of odd :",odd_count)

