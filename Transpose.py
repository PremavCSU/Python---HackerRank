import numpy as np

#numbers = input().split()
r,c =list(map(int, input().split() )) #read input as row(r) and column(c)

## 2. Read the matrix rows and store them in a list 
matrix = []

for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

print("matrix:", matrix)
# 3. Convert the list to a NumPy array
arr = np.array(matrix)
#print(arr.T)
# 4. Print the Transpose of the array

print("transpose:", arr.transpose())
print("transpose T:", arr.T)

# 5. Print the Flattened version
print("flattened:", arr.flatten())