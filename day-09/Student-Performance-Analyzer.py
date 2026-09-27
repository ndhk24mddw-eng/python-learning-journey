# Student Performance Analyzer
students = [
    ["Ronak", 78, 85, 91, 67, 88],
    ["Aman", 65, 72, 80, 75, 69],
    ["Priya", 92, 88, 95, 90, 94],
    ["Rahul", 45, 55, 61, 50, 48]
]
print(students[0])
print(students[-1])
print(students[0][-2])
print(students[0 : : 2])

#Add a new student.
students.append(['ravi',56,55,55,34,45,])
print(students[0])

#Delete a student.
students.pop(-2)
print(students)



#Update marks.
students[0][1] = 95
print(students[0])

# #total marks o ronak
# marks = students[0][1:6]
# total_ronak_marks = sum(marks)
# print('Total marks obtained',total_ronak_marks )
# length = len(marks)
# avg = total_ronak_marks/length
# print('Average of the marks is :',avg)
# print('maxium marks obtained by ronak :',max(marks))
# print('Minimum marks obtaind by ronak :',min(marks))

for student in students:
    print('Name of the student is :',student[0])
    marks = student[1:6]
    result = "PASS"

    for i in marks:
        if i < 40:
             result = "FAIL"
    print(result)
    total_marks = sum(marks)
    print(total_marks)
    Average = total_marks/len(marks)
    print('average :',Average)
    print('maxium marks  :',max(marks))
    print('Minimum marks  :',min(marks))

    if Average >= 90:
        print('Grade A+')
    elif Average >= 80:
        print('Grade A')
    elif Average >= 70:
        print('grade B')
    elif Average >= 60:
        print('Grade C')
    elif Average >= 50:
        print('Grade D')
    else:
        print('grade D')

for i in range(1,6):
    marks = []
    for student in students:
        marks.append(student[i])
    print(marks)

for mark in marks:
    print(marks)



