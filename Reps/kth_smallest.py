"""
Given: unsorted array
Want: k-th smallest number

Idea:
- push k elements into max heap
- as encounter smaller than top, pop off
- push new in
- top at end = kyth smallest

USE: Quickselect
- partition in O(n) best, O(n^2) worst

Approach:
- pick pivot
- partition input array around it
- left = smaller , right =  larger or equal
- pivot in corrected sorted position
- if pivot position > k-1
    - recursively partition lower bit
- if pivot position < k-1
    - recursively partition higher bit

Complexity:
- best and average: O(n)
- wrost = O(n^2)
- quicksort only searches one side
- worst case = bad pivot

WHY: O(n)
- every iteration, let's say exactly half
- each iteration is N + n/2 + n/4  . .  < 2 * N
    (geometric summing, close to but never 1)
- wosrt case: N + (N-1) + (N-2)
"""

def solve(nums, k):
    return find_kth(nums, k, 0, len(nums)-1)

def find_kth(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k-1:    #found the value
        return nums[p]
    
    if p> k-1: #search lower
        return find_kth(nums, k, start, p-1)
    
    return find_kth(nums, k, p+1, end)

def partition(nums, low, high):
    if low == high:
        return low
    
    pivot = nums[high]

    for i in range(low, high):
        if nums[i] < pivot: #partition/throw it around
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
    
    #put in position
    nums[low], nums[high] = nums[high], nums[low]
    return low

"""
PIVOT STRATEGY:
Median of Medians O(n)
- need O(n) trime

- if 5 or less elements, return first as median
- sort each arr for median
    (fixed sized array sort = constant time)
- get array of medians of subarraays
- recursively call, until pivot

USE: within each partition call
that needs a pivot

"""

def median_of_medians(nums, low, high):
  n = high - low + 1
  # if we have less than 5 elements, ignore the partitioning algorithm
  if n < 5:
    return nums[low]

  # partition the given array into chunks of 5 elements
  partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

  # for simplicity, lets ignore any partition with less than 5 elements
  fullPartitions = [
    partition for partition in partitions if len(partition) == 5]

  # sort all partitions
  sortedPartitions = [sorted(partition) for partition in fullPartitions]

  # find median of all partations; the median of each partition is at index '2'
  medians = [partition[2] for partition in sortedPartitions]

  return partition(medians, 0, len(medians)-1)
