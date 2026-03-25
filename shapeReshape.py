import numpy as np

#n = input()

numbers = input().split()

num_list = list(map(int, numbers))

arr = np.array(num_list)

arr_shape = arr.reshape(3, 3)

print(arr_shape)

