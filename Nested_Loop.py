#nested loop Python program

''' 
Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

student = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]

Sample Output 0

Berry
Harry

'''

n = int(input("Enter number of studnets: "))
student = []

for _ in range(n):
    name = input("Enter student name: ")
    scores = float(input("Enter student marks: "))
    student.append([name, scores])

scores = []

for s in student:
    scores.append(s[1]) # append only scores from the student lsit

scores = list(set(scores)) # remove duplicates scores using set() 
scores.sort() #sort the scoring list in ascending order 

second_lowest = scores[1] # get the second lowest score

name = []
for s in student:
    if s[1] == second_lowest:
        name.append(s[0]) # append the name of the student with second lowest score

name.sort() # sort the list of names in ascending order

for n in name:
    print(n) # print each name on a new line

print(student)
print(scores)
print(second_lowest)

