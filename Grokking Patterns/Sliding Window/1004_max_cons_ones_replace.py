"""
STATEMENT:
Given: binary array, int k
Want: max number of consecutive 1's
- can flip at most k 0-es

STRATEGY:
- sliding window
- max_lent, wind_start
- iterate until hit k non-1es
- shrink until back to same
- for each shrink, check if popped a 0, if so, no more shrinking

"""

def length_longest_substring(arr, k):
    """
    TIME: O(n)
    Space: O(1)
    """
    wind_start, max_lent, max_count = 0, 0, 0

    for wind_end in range(len(arr)):
        if arr[wind_end] == 1:
            max_count += 1
        
        if (wind_end - wind_start +1 - max_count) > k:
            if arr[wind_start] == 1:
                max_count -= 1
            wind_start += 1
    
        max_lent = max(max_lent, wind_end - wind_start +1)
    
    return max_lent