"""
Given: int array, int target
Want: three ints, sum closest to target

Strategy:
- sort array
- iterate over
- for each iterate find the closest sum p air
- save it
"""

import math

def triplet_sum_close(arr, target):
    arr.sort()
    min_diff = math.inf
    for i in range(len(arr)-2):
        left = i+1  #don't repeat search
        right = len(arr) - 1
        while left < right:
            target_diff = target - arr[i] - arr[left] - arr[right]
            if target_diff == 0:    #found exact triplet
                return target - target_diff
            
            #saving result
            if (abs(target_diff) < abs(min_diff)) or \
             (abs(target_diff) == abs(min_diff) and target_diff>min_diff):
                min_diff = target_diff
            
            if target_diff > 0:
                left +=1
            else:
                right -= 1
    
    return target - min_diff