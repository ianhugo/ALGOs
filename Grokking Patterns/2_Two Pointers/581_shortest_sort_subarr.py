"""
Given: array unsorted
Want: smallest subarray, with sorted, sorts all

STRATEGY
- two pointers
- note the smallest and biggest
- from right, note smallest 
- from left, note the first bigger than left smallest
- start from both ends
- if at any point, left > right, mark and return
- if left < right, check if next one of both 
is correct order, if not pointer stays

Approach
- from left: find first that is smaller than prev
- from right: find first that is larger than prev
- find max, min of window
- extend left to include all bigger than min
- extend right to include all smaller than max

Learned:
- don't become fixated by the time complexity
- solve the problem first
- hacky solution is ok, optimize later
- set out "principles" or "axioms" or "theorems"
"""

import math

def shortest_window_sort(arr):
    """
    O(n) time
    """
    low, high  = 0, len(arr)-1

    #while within bounds
    #curr smaller than next
    while (low < len(arr)-1 and arr[low] <= arr[low+1]):
        low += 1
    
    #sorted
    if low == len(arr)-1:
        return 0
    
    while (high>0 and arr[high] >= arr[high-1]):
        high -= 1
    
    sub_max = -math.inf
    sub_min = math.inf

    #locate max, min
    for k in range(low, high +1):
        sub_max = max(sub_max, arr[k])
        sub_min = min(sub_min, arr[k])
    
    #extend subarray
    #to left, numbers bigger than sub_min 
    while (low>0 and arr[low-1] > sub_min):
        low -= 1
    
    #to right, numbers smaller than sub_max
    while (high < len(arr)-1 and arr[high+1 < sub_max]):
        high +=1
    
    return high - low +1