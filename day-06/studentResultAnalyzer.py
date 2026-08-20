# Mini Project 1 — Student Result Analyzer

# Build a small Python program that takes marks for 5 subjects and produces a complete result.

# Your program should:

# Take student name.
# Take marks for 5 subjects:
# Python
# DSA
# DBMS
# SEPM
# Computer Networks
# Validate marks:
# Marks must be between 0 and 100.
# If any mark is invalid → print "Invalid marks" and stop.
# Calculate:
# Total
# Percentage
# Determine result:
# Any subject < 40 → FAIL
# Otherwise → PASS
# Determine grade:
# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 40–59 → E
# Print a clean result.

# Example:

# Enter student name: Ronak


# Python: 85
# DSA: 78
# DBMS: 91
# SEPM: 82
# CN: 88


# ========== RESULT ==========
# Name: Ronak
# Total: 424
# Percentage: 84.8%
# Result: PASS
# Grade: B
# ============================




name = input("Enter Student name :")
DSA = int(input("Enter DSA  marks :"))
if DSA < 0 or DSA >100:
    print("please enter a valid marks :")
    exit()    

DBMS = int(input("Enter DBMS  marks :"))
if DBMS <0 or DBMS >100:
    print("please enter a valid marks :")
    exit()    

SEPM = int(input("Enter SEPM  marks :"))
if SEPM < 0 or SEPM >100:
    print("please enter a valid marks :")
    exit()    

Maths = int(input("Enter Maths marks :"))
if Maths < 0 or Maths >100:
    print("please enter a valid marks :")
    exit()    

Python = int(input("Enter Python  marks :"))
if Python < 0 or Python >100:
    print("please enter a valid marks :")
    exit()    

#calculate total marks

totalMarks = DSA+SEPM+DBMS+Maths+Python
totalPercentage = totalMarks / 5



if DSA < 40 or DBMS < 40 or SEPM < 40 or Maths < 40 or Python < 40:
    result = "FAIL"
else:
    result = "PASS"


print("========== RESULT ==========")
print("Name:", name)
print("Total:", totalMarks)
print("Percentage:", totalPercentage)

# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 40–59 → E

if result == "FAIL":
    grade = "F"
else:
    if totalPercentage >= 90:
        grade = "A"
    elif totalPercentage >= 80:
        grade = "B"
    elif totalPercentage >= 70:
        grade = "C"
    elif totalPercentage >= 60:
        grade = "D"
    else:
        grade = "E"

print("Grade:", grade)