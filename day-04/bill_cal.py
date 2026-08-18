# Condition — Hard Problem 1: Electricity Bill Calculator

# Write a Python program that takes the number of electricity units consumed and calculates the bill.

# Rules:

# 0–100 units       → ₹5 per unit
# 101–200 units     → ₹7 per unit
# 201–300 units     → ₹10 per unit
# Above 300 units   → ₹12 per unit

# The billing is progressive.

# Example:

# Input: 350 units


# First 100  → 100 × 5  = ₹500
# Next 100   → 100 × 7  = ₹700
# Next 100   → 100 × 10 = ₹1000
# Next 50    → 50 × 12   = ₹600


# Total = ₹2800

# Additional rules:

# If units are negative → print Invalid units
# If units are 0 → bill is ₹0
# Calculate and print the final bill.

# Do not use any library or built-in billing function.

unit = int(input("Enter the unit: "))

if unit < 0:
    print("Please enter a valid input")
    exit()

if unit <= 100:
    print("Your electricity bill is:", unit * 5)

elif unit <= 200:
    print("Your electricity bill is:", 500 + (unit - 100) * 7)

elif unit <= 300:
    print("Your electricity bill is:", 500 + 700 + (unit - 200) * 10)

else:
    print("Your electricity bill is:", 500 + 700 + 1000 + (unit - 300) * 12)


