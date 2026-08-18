# Write a program that takes a student's marks in 5 subjects and calculates:

# Total marks
# Percentage
# Grade

# Assume each subject is out of 100.


# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# Below 60 → F


math = int(input("Enter the marks obtained in Math: "))
DSA = int(input("Enter the marks obtained in DSA: "))
sepm = int(input("Enter the marks obtained in SEPM: "))
DBMS = int(input("Enter the marks obtained in DBMS: "))
python = int(input("Enter the marks obtained in Python: "))

totalmarks = math + DSA + sepm + DBMS + python
percentage = totalmarks / 5

print("Total marks:", totalmarks)
print("Percentage:", percentage)

if math < 40 or DSA < 40 or sepm < 40 or DBMS < 40 or python < 40:
    print("Grade: F")
    print("Result: Fail")

elif percentage >= 90:
    print("Grade: A")

elif percentage >= 80:
    print("Grade: B")

elif percentage >= 70:
    print("Grade: C")

elif percentage >= 60:
    print("Grade: D")

else:
    print("Grade: F")