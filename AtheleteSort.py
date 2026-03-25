import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read n (rows) and m (columns)
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    # Build the 2D array
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Read the index k to sort by
    k = int(input())

    # Sort the array in-place using the k-th element of each row as the key
    arr.sort(key=lambda x: x[k])

    # Print the sorted rows
    for row in arr:
        print(*row)