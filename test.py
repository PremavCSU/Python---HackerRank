def solution(a):
    n = len(a)
    result = []
   
    for i in range(n):
        found_val = -1
        # We check distances d = 1, 2, 3... until we find a match or hit the edge
        for d in range(1, n):
            left = i - d
            right = i + d
           
            # Check left first (per your preference for the "first" or "most" one)
            if left >= 0 and a[left] > a[i]:
                found_val = a[left]
                break
            # Check right
            elif right < n and a[right] > a[i]:
                found_val = a[right]
                break
           
            # If we've reached the point where both left and right are out of bounds
            if left < 0 and right >= n:
                break
               
        result.append(found_val)
   
    return result
input_array = [4, 2, 1, 7, 6]
output = solution(input_array)
print(output) # output array is [7, 4, 2, -1, 7] 