# Students who study all three subjects.
# Students who study Python and DSA but NOT DBMS.
# Students who study only DBMS — they don't study Python or DSA.
# Students who study at least one subject.
# Students who study exactly two subjects.
python = {"Ronak", "Aman", "Rahul", "Priya", "Neha"}
dsa = {"Ronak", "Rahul", "Neha", "Vikas", "Aman"}
dbms = {"Ronak", "Aman", "Karan", "Neha"}

python = {"Ronak", "Aman", "Rahul", "Priya", "Neha"}

dsa = {"Ronak", "Rahul", "Neha", "Vikas", "Aman"}

dbms = {"Ronak", "Aman", "Karan", "Neha"}


# 1. Students who study all three subjects
all_three = python & dsa & dbms

print("Students who study all three:", all_three)


# 2. Students who study Python and DSA but NOT DBMS
python_dsa_only = (python & dsa) - dbms

print("Python and DSA but NOT DBMS:", python_dsa_only)


# 3. Students who study only DBMS
only_dbms = dbms - (python | dsa)

print("Students who study only DBMS:", only_dbms)


# 4. Students who study at least one subject
at_least_one = python | dsa | dbms

print("Students who study at least one:", at_least_one)


# 5. Students who study exactly two subjects

python_dsa = (python & dsa) - dbms

python_dbms = (python & dbms) - dsa

dsa_dbms = (dsa & dbms) - python

exactly_two = python_dsa | python_dbms | dsa_dbms

print("Students who study exactly two:", exactly_two)
