#nested loop Python program

student = []

for i in range(3):
    name = input()
    marks = float(input())
    student.append([name, marks])

    print(student)