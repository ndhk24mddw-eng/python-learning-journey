# Topic: Conditions
# Concepts: if, elif, else, comparison
#  operators, logical operators, input validation

# Problem:

# Create a program that takes marks for 5 subjects:

# Python
# DBMS
# Computer Architecture
# Mathematics
# Digital Electronics

# Calculate:

# Total marks
# Percentage
# Result: PASS or FAIL
# Grade

# Rules:

# If any subject is below 40, the student fails.
# Otherwise:
# 90–100 → A+
# 80–89 → A
# 70–79 → B
# 60–69 → C
# 50–59 → D
# 40–49 → E

# Also validate the input:

# Marks cannot be below 0.
# Marks cannot be above 100.

# If invalid marks are entered, print:

# Invalid marks

Python = int(input('Enter your pyhton marks :'))
if Python>100 or Python<0:
    print('Invalid marks :')
    exit()

if Python<40:
    print(' Fail in this subject :')
    

DBMS = int (input('Enter your DBMS marks :'))
if DBMS > 100 or DBMS<0:
    print('Invalid Marks :')
    exit()

if DBMS<40:
    print('Fail in this subject :')
 

CA = int (input('Enter your CA marks :'))
if  CA >100 or CA<0:
    print('Invalid marks :')
    exit()

if CA<40:
    print('Fail in this subject :')
    

Math = int(input('Enter your Math marks :'))
if Math > 100 or Math<0:
    print('Invalid marks :')
    exit()

if Math<40:
    print('Fail in this subject :')
    

DE = int(input('Enter your DE marks :'))
if DE > 100 or DE <0:
    print('Invalid marks :')
    exit()

if DE<40:
    print('Fail in this subject :')
    

Total_Marks = Python+DBMS+CA+Math+DE
print('Total marks of the student is :',Total_Marks)
Percentage = Total_Marks/5
print('Total Percentage of the student is :',Percentage)

if Percentage <=100 and Percentage >=90:
    print('Grade A+')
elif Percentage <90 and Percentage >=80:
    print('Grade A')
elif Percentage <80 and Percentage >=70:
    print('Grade B')
elif Percentage <70 and Percentage >=60:
    print('Grade C')
elif Percentage <60 and Percentage >=50:
    print('Grade D')
elif Percentage <50 and Percentage >=40:
    print('Grade E')
else:
    print('FAIL :')


