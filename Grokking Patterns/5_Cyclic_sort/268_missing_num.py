"""
Given: arr of n distinct numbers
Want: the missing number out of n+1 numbers

Observe:
missing number means there is a duplicate
normal cyclic sort, if already put there, then will not switch again
when it finishes, the duplicate will be at missing number index

iterate through again to find it


LEARNED:
- careful with indexing for these questions
- careful with stopping conditions

Clever:
use Gaussian formula, sum up all
then the difference is what number is missing

"""

def find_missing(nums):
    """
    O(n) time
    O(1) space
    """
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        #within range, and number not in place
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n