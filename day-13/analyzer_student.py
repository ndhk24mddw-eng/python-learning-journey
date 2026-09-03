# The total marks obtained by each student.
# The average marks of each student.
# The student with the highest total marks.
# The subjects in which any student scored below 70.
# The set of all unique students.
# The set of all unique subjects.

students = (
    ("Ronak", "Python", 85),
    ("Aman", "Python", 72),
    ("Rahul", "Python", 91),
    ("Ronak", "DSA", 78),
    ("Aman", "DSA", 88),
    ("Rahul", "DSA", 95),
    ("Ronak", "DBMS", 92),
    ("Aman", "DBMS", 65),
    ("Rahul", "DBMS", 89)
)


def analyze_students(students):

    totals = {}
    counts = {}
    below_70 = set()
    unique_students = set()
    unique_subjects = set()

    # Process every student record
    for name, subject, marks in students:

        unique_students.add(name)
        unique_subjects.add(subject)

        # Calculate total marks
        if name not in totals:
            totals[name] = marks
            counts[name] = 1
        else:
            totals[name] += marks
            counts[name] += 1

        # Find subjects where marks are below 70
        if marks < 70:
            below_70.add(subject)

    # Calculate average
    averages = {}

    for name in totals:
        averages[name] = totals[name] / counts[name]

    # Find highest student
    highest_student = ""
    highest_total = 0

    for name, total in totals.items():

        if total > highest_total:
            highest_total = total
            highest_student = name

    return (
        totals,
        averages,
        highest_student,
        highest_total,
        below_70,
        unique_students,
        unique_subjects
    )


# Calling function

result = analyze_students(students)

totals = result[0]
averages = result[1]
highest_student = result[2]
highest_total = result[3]
below_70 = result[4]
unique_students = result[5]
unique_subjects = result[6]


# Display result

for name in totals:
    print(name)
    print("Total:", totals[name])
    print("Average:", round(averages[name], 2))
    print()


print("Highest Student:", highest_student)
print("Highest Total:", highest_total)

print()

print("Subjects having marks below 70:")
print(below_70)

print()

print("Unique Students:")
print(unique_students)

print()

print("Unique Subjects:")
print(unique_subjects)

