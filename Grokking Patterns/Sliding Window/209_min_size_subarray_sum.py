"""
STATEMNET:
Given: array, int K
Want: find min length
of subarray 
that has sum greater than or equal to K

OBSERVATIONS:
- when finding length things in sliding window
    - stretch until meet length requirement
    - when meet, shrink window
    - if shrink too much, add new
"""

import math

def smallest_subarray_given_sum(s, arr):
    """
    TIME: O(n+n)
    outer: n loops
    while loop: process each element once

    SPACE: O(1)
    
    """
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        
        #add next element
        window_sum += arr[window_end]

        #shrink window to smallest
        #until window_sum smaller than s
        #(violate requirement)

        while window_sum >= s:
            curr_len = window_end - window_start +1
            min_length = min(min_length, curr_len)
            window_sum -= arr[window_start]
            window_start += 1
        
    if min_length == math.inf:
        return 0
    return min_length