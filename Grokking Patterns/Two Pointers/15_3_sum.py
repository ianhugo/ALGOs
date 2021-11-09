"""
Given: unsorted integer arr
Want: all triplets, sum to 0

Strategy:
- sort the array
- iterate through
- for each iterate do two sum, for the negative number of idx

Hash Strategy:
find complement in hash
store found elements
"""

def search_triplets(arr):
    """
    O(n lg n ) sort time
    O(n^2) runtime

    O(n) space
    """
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
    search_pair(arr, -arr[i], i+1, triplets)

    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target_sum:   #found triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1   #keep going to find more
            right -= 1

            #skipping duplicates
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -=1
        
        elif target_sum > cur_sum: #need bigger
            left += 1
        else:   #need smaller
            right -=1