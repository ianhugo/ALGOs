"""
Given: array of values
Want: maximum value
Constraint: no adjacent visits

max value, for overall jumps
"""


def solve(arr):
    return recur(arr, 0)

def recur(arr, curr_idx):

    #out of bounds, no profits
    if curr_idx >= len(arr):
        return 0
    
    do_curr = arr[curr_idx] + recur(arr, curr_idx+2)
    skip_curr = recur(arr, curr_idx+1)

    return max(do_curr, skip_curr)

"""Top-Down"""
#main issue: how to cover all cases, make sure all cases covered

def solve1(arr):
    dp = [0 for x in range(len(arr))]
    return recur(dp, arr, 0)

def recur1(dp, arr, curr_idx):

    #out of bounds, no profits
    if curr_idx >= len(arr):
        return 0
    
    if dp[curr_idx] == 0:

        do_curr = arr[curr_idx] + recur(arr, curr_idx+2)
        skip_curr = recur(arr, curr_idx+1)
        dp[curr_idx] = max(do_curr, skip_curr) 

    return dp[curr_idx]

"""Bottom-up"""

def solve2(arr):

    n = len(arr)

    if n == 0:
        return 0
    
    dp = [0 for x in range(n+1)]
    dp[0] = 0       #padded
    dp[1] = arr[0]

    for i in range(1, n):
        dp[i+1] = max(arr[i] + dp[i-1], dp[i])
        #choose current house, and two houses back (rob)
        #choose last house (skip)
    
    return dp[n]

"""Space Optimized"""

def solve3(arr):
    n = len(arr)

    if n == 0:
        return 0
    
    n1, n2 = 0, arr[0]

    for i in range(1, n):
        n1, n2 = n2, max(n1 + arr[i], n2)
    
    return n2

"""Bottom-up 2"""

def solve4(arr):
    if not arr:
        return 0
    
    n = len(arr)

    dp = [None for _ in range(n+1)]

    dp[n], dp[n-1] = 0, arr[n-1]

    for i in range(n-2, -1, -1):
        dp[i] = max(dp[i+1], dp[i+2]+ arr[i])
    
    return dp[0]


#at each step, what are the choices

#assume robbed, skip how far
#vs
# robbed or not robbed
#make sure to go down down down to the first decision
#pad value one back
