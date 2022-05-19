"""
Given: unsorted arr of integers, k
Want: number of contiguous subarrays
product of elements < k

Strategy: 
- sliding window

LEARNED:
counting stuff,
note count multiple times, can be embedded in a loop


"""

from collections import deque

def find_subarr(arr, target):
    """
    O(n) sliding window
    O(n^2) creating subarray

    strategy:
    1: target with sliding window
    multiply and enlarge a product var
    when over target, shrink, divide product
    2: add with two pointers
    (this happens at the end of each main loop, never skipped)
    with new window, go from right to left
    add most right then first (adds all subarrays)
    """
    result = []
    product = 1
    left = 0

    #sliding the window
    for right in range(len(arr)):
        product *= arr[right]

        #when hit the target, shrink window
        while (product >= target and left<len(arr)):    
            #checking each = allow for negatives
            product /= arr[left]
            left += 1 #shrink   
        
        temp_list = deque() #this allows singles to be included as well
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])    #at each iter, add one
            result.append(list(temp_list))
            #at end of iter, have added the whole array from right to left
            #thus singles, and multiples included
            #this avoids duplicate subarrays, because this loop enters at every iter
    
    return result

#if all are positive
#then don't need to iterate backwards and include
def find_subarr_pos(arr, target):
    """
    O(n) time
    O(1) space
    """
    if target <= 1:
        return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(arr):
        prod *= val
        while prod >= target:
            prod /= arr[left]
            left += 1   #incremented at most n times
        ans += right - left +1  # this is the key
    
    return ans

"""
BINARY SEARCH ON LOGs
as log of (product of x-es) = sum of log(x) -es
use subarray sums instead
- log all values
- take prefix sums
pref[i] = arr[0] + arr[1] . . + arr[i]
for each i find j
arr[i] . . .+ arr[j] = pref[j] - pref[i] < target
as pref = monotone increasing array, use binary search
"""
import math

def log_sol(arr, target):
    """
    O(n lg n) time
    O(n) space for prefix
    """
    if target ==0:
        return 0
    
    target = math.log(target)
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1]+ math.log(x)) #add with latest one
    
    ans = 0

    for i, x in enumerate(prefix):
        j = bisect.bisect(prefix, x)
        ans += j - i -1 #width of interval
    
    return ans

