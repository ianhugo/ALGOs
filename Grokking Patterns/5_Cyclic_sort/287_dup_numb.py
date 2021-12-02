"""
Given: unsorted index arrays
Want: the duplicate
"""
#OBSERVE: if numbers switching are the same, then it is the duplicate

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1



"""
Without modifying the array?

STRATEGY: 
- fast and slow poitners
- slow pointer = start at 0
- fast pointer = start at correc tpos of the number at index 0
- while not equal, keep looping
- stop = found a duplicate

Intuition:
nums[x], nums[nums[x]], nums[nums[nums[x]]],
- go to the real place of that number
- if duplicate, will go to the real place twice
- thus there is a cycle
- with fast slow pointers, will meet at a duplicate

Learned:
Cyclic sort -> linked list/cycle

O(n) time
"""

def find_duplicate(arr):
    slow, fast = arr[0], arr[arr[0]]

    #fast, slow pointers
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    # go until hit original start again
    current = arr[arr[slow]]
    cycleLength = 1
    while current != arr[slow]:
        current = arr[current]
        cycleLength += 1

    return find_start(arr, cycleLength)

def find_start(arr, cycleLength):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while cycleLength > 0:
        pointer2 = arr[pointer2]
        cycleLength -= 1

    # increment both pointers until they meet at the start of the cycle
    #go through cycle until meet
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    #return meet point/cycle entrance
    return pointer1