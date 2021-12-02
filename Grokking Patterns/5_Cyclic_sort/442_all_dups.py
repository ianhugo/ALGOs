"""
Easier, can alter
Given: unsorted array of range numbers
Want: all duplicate numbers
O(1) space

Strategy:
Cyclic Sort
- use while loop
- if not match index, append
- then increment i to skip forward
- keep checking
O(n)

"""

def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    dups = []
    counted = 0
    while i < len(nums):
        if nums[i] != i+1:
            dups.append(nums[i])
            
            if counted > 1:
                i += 1
            if nums[i] == nums[i-1]:
                counted += 1
            
        i+= 1
    
    return dups



