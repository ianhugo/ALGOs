"""
Given: unsorted array of integers
Want: smallest missing positive integer

O(n) time
O(1) space

StrategY:
Exclude negative numbers
- throw all negative numbers to LHS, increment pointer to border

Exclude numbers larger than length

Check if 1 is there, check if 2 is there . . .
HOW?
sort the subarray -> O n lg n


- iterate through 1 to n, positive numbers


LEARNED:
- exclude numbers larger than range
"""

"""
O(N) time
O(1) space
"""

def find_smallest(nums):
    i, n = 0, len(nums)
    while i< n:
        j = nums[i] - 1
        #if nnon negative, not out of range, and not match
        #then cyclic sort
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1  #skip over
    
    for i in range(n):  #now all the relevant numbers are in place
        if nums[i] != i+1:  #so stop at earliest
            return i+1
    #if all matched 
    # or there are way larger positive numbers
    # then it is the next number
    return len(nums) +1 


"""
Interesting Solution

Use index as hash key
Use sign of element at index, as hash value

So nums[2] has a -ve sign, means 2 is present
be careful with duplicates to only change sign once


OVERVIEW:
1. check if 1 is present = stop early
2. Knix Negative numbers, Zeros, numbers larger than length
3. iterate over, when encounter element, change sign of related index
4: iterate again, return index of first positive element

O(n) time
O(1) space
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1