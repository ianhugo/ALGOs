"""
STATEMENT:
Given: array, target sum
Want: pair of indices, that sum to target

Strategy:
Two-pointers

Hash Strategy:
iterate through once
store hashes of numbers
for each number check if the differenced is in hash
if so return

"""

def two_sum(arr, target):
    """
    O(n) time
    O(1) space
    """
    left, right = 0, len(arr)-1

    while left<right:
        curr_sum = arr[left] + arr[right]
        
        if curr_sum == target:
            return [left, right]
        
        if target > curr_sum:
            left +=1
        else:
            right -=1
    
    return [-1, -1]
