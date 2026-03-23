def nearest_larger(arr):
    n = len(arr)
    result = [-1] * n
    
    for i in range(n):
        left_dist = float('inf')
        right_dist = float('inf')
        
        # Look left
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                left_dist = i - j
                break
        
        # Look right
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                right_dist = j - i
                break
        
        # Tie-breaker logic: pick left if dist is same or smaller
        if left_dist <= right_dist and left_dist != float('inf'):
            result[i] = arr[i - left_dist]
        elif right_dist != float('inf'):
            result[i] = arr[i + right_dist]
            
    return result

# Test
print(nearest_larger([4, 2, 1, 7, 6])) # Output: [7, 4, 2, -1, 7]