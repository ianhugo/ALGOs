"""
Given: arr of distinct ints
Want: all possible permutations
permutation = order matters

Change: each new elements need to be added in 
different positions
"""

"""
O(n * n!) time and space
"""
from collections import deque

def find_perms(nums):
    lent = len(nums)
    res = []
    perms = deque()
    perms.append([])

    for curr in nums:
        n = len(perms)

        for _ in range(n): #for each current perm
            old_perms = perms.popleft() #don't need this?

            #adding to all positions
            for j in range(len(old_perms)+1):
                new_perms = list(old_perms)
                new_perms.insert(j, curr) #insert diff positions
                if len(new_perms) == lent: #last element added
                    res.append(new_perms)
                else:
                    perms.append(new_perms)
    
    return res



#####recursion
def generate_permutations(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
  if index == len(nums):
    result.append(currentPermutation)
  else:
    # create a new permutation by adding the current number at every position
    for i in range(len(currentPermutation)+1):
      newPermutation = list(currentPermutation)
      newPermutation.insert(i, nums[index])
      generate_permutations_recursive(
        nums, index + 1, newPermutation, result)

