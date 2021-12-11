"""
Implement this function
Given: array
Want: next highest ordering
(or the lowest possible one)

Intuition:
- if descending, then it is largest, reverse
- if not, then iterate from back
- find a[i] < a[i-1] (first decreasing)
- iterate backwards, find number closest (from upper) to a[i]
- swap
- reverse a[i-1:]

"""

def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1