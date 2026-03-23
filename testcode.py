
#specifically O(n) time complexity— 
#Monotonic Stack 

def solution(a):
    n = len(a)
    left_larger = [-1] * n
    right_larger = [-1] * n
    
    # Pass 1: Find nearest larger to the LEFT
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            left_larger[i] = stack[-1]
        stack.append(i)
        
    # Pass 2: Find nearest larger to the RIGHT
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            right_larger[i] = stack[-1]
        stack.append(i)
        
    # Final step: Compare distances
    res = []
    for i in range(n):
        l_idx = left_larger[i]
        r_idx = right_larger[i]
        
        if l_idx == -1 and r_idx == -1:
            res.append(-1)
        elif l_idx != -1 and r_idx == -1:
            res.append(l_idx) # Only left exists
        elif l_idx == -1 and r_idx != -1:
            res.append(r_idx) # Only right exists
        else:
            # Both exist: check distance
            if (i - l_idx) <= (r_idx - i): # Distance check (tie-break prefers left)
                res.append(l_idx)
            else:
                res.append(r_idx)
    
    return res