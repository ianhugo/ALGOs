"""
Given: unsorted array, k
Want: k missing numbers in array

Strategy:

Enter:
Shoudl we sort?

Do what we did for first missing pos, but keep iterating
"""


"""
O(n+k)

O(n) two loops
O(k) last loop

O(k) space, to store extra numbers and missing numbers
"""

def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    #cyclic sort, and leave out negatives
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missingNumbers = []
    extraNumbers = set()    #this is key

    #normal find first few positives
    for i in range(n):  #iterate
        if len(missingNumbers) < k: #while still need more
            if nums[i] != i + 1:    #is this index matching
                missingNumbers.append(i + 1)    #if not then append the index, i+1
                extraNumbers.add(nums[i])       #add to extranumbers
    
    #by now extra numbers have all out of range ones, as well as negatives
    #now iterate more

    # add the remaining missing numbers
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        # ignore if the array contains the candidate number
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
            i += 1

    return missingNumbers


"""
Given: sorted array
Want: kth missing number

Approach:
- use binary search
- compare current array, with a correct array of form [1, 2, 3 . .]
- do difference between
- differenced (val = x) at idx 1= before arr[1], 
    = there are x missing numbers before idx1 element
    and so on . .
- choose pivot to be middle of array
- if number of +ve integers, missing before arr[pivot] < k
- search on right side
- otherwise, search on left side
- at the end:
    left = right +1
    kth missing between arr[right] and arr[left]
    number of missing before arr[right] = arr[right] - right -1
    arr[right] + k - (arr[right] - right - 1) = k + left
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k