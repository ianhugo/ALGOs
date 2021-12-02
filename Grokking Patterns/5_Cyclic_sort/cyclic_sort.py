"""
Given: array of n objects
each object numbered within range
Say: 1 to n

Want: sort objects in place
in O(n) time, O(1) space

Enter:
key diff: given the range

Strategy:
Iterate over
at each idx,
if not correct pos, switch with its correct idx

"""

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1 #what is in the correct position
        if nums[i] != nums[j]:  #has it been placed already
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums
