# Students studying both Python and DSA
# Students studying Python or DSA
# Students studying Python but not DSA
# Students studying DSA but not Python

python_students = {"Ronak", "Aman", "Rahul", "Priya", "Neha"}

dsa_students = {"Ronak", "Rahul", "Neha", "Vikas", "Aman"}

print("Students studying both Python and DSA :",python_students & dsa_students)
print("Students studying Python or DSA :",python_students|dsa_students)
print("Students studying Python but not DSA :",python_students - dsa_students)
print("Students studying DSA but not python :", dsa_students-python_students)

