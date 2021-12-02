"""
Given: array of numbers
each number = max jump
Want; minimum number of jumps to reach the end

Enter:
starting from 0, want to get to -1

at each step, want to jump to square with maximal distance
if combined with oneself

Why FIB?
- solution to longer range
- depend on solution to shorter range


Brute IDEA:
- start with 0
- go to all reachable from that
- store the steps taken to new
- if empty, store steps
- if not, take minimum
- keep going until hit the end

Top-Down Idea:
- O(n^2)
- at each node, look at next arr[i] nodes
- can have at most n nodes


"""

import math

def solve(arr):
    n = len(arr)
    dp = [0 for _ in range(n+1)]    #n+1 as need base case
    min = recur(dp, arr, n, 0)
    return min

def recur(dp, arr, n, curr_idx):

    if curr_idx ==n-1:
        return 1
    
    if arr[curr_idx] ==0:   #not end, and deadend
        return math.inf
    
    min1 = math.inf
    if dp[n] == 0:
        for i in range(1, arr[n]+1):
            if dp[n+i]!= 0:
                min1 = min(min1, dp[n+1])
            else:
                min1 = min(min1, recur(dp, arr, n, n+i))

        dp[n] = min1
    else:
        return dp[n]
    
    return dp[n]
]

"""BRUTE"""

def solve(arr):
    n = len(arr)
    return recur(arr, n, 0)

def recur(arr, n, curr_idx):

    if curr_idx == n-1: #no more jumps needed
        return 0
    
    if arr[curr_idx] ==0:   #not end, and deadend
        return math.inf
    
    #check cache (top-down)

    total = math.inf

    #range of motion
    start, end = curr_idx +1, curr_idx + arr[curr_idx]

    while start < n and start <= end:

        min = recur(arr, n, start)

        if min != math.inf: #not dead end
            total = min(total, min+1)   #take min
        
        start += 1  #iterate
    
    #store cache (top-down)

    return total

"""Bottom-Up

- initialize dp array
- dp[0] = 0
- dp[1] = 1

after that, 
check if can reach end
if not: loop through from furthest can reach, +1
find the minimum
put this as solution
"""


#this is O(n^2)
def count(arr):
    n = len(arr)

    dp = [math.inf for _ in range(n)]

    dp[0] = 0

    for start in range(n-1):
        end = start+1
        #loop from adjacent, to max range
        #while max range is less than n
        #each endpoint, do min
        while end <= start + arr[start] and end < n:
            dp[end] = min(dp[end], dp[start]+1)
                #if want backtrack, need to store parent array
            end += 1
    
    return dp[n-1]



"""Greedy O(n)

at each point, choose the location
that can take us to the farthest point"""

def solve(arr):
    jumps = 0
    curr_jump_end = 0
    farthest = 0

    for i in range(len(arr)-1):
        farthest = max(farthest, i + arr[i])
        #calculate the farthest we can reach at this point

        #starting at 0, thus always enter
        #after that, only enters when we are at index of last farthest
        #finished current jump
        if i == curr_jump_end:
            jumps += 1
            curr_jump_end = farthest
    
    return jumps

"""
Consider range of effect O(n)
move range of effect
each range of effect, calculate next range of effect
"sliding window"

keep creating new windows, ranges of effect
increment jump
stop when range of effect can reach the end

NOTE: just storing number of jumps
NOTE:  changing window size
"""
def jump2(arr):
    jumps = 0
    farthest = 0
    left = right = 0

    while right < len(arr)-1: #once window touches, then can stop
        for i in range(left, right+1):
            farthest = max(farthest, i + arr[i])
        
        left = right+1
        right = farthest
        jumps += 1
    return jumps