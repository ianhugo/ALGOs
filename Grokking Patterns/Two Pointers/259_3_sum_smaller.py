"""
Given: unsorted array
Want: count all triplets with sum smaller than target"""

def trip_small_sum(arr, target):
    """
    O (n lg n) sort
    O(n^2)
    """
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += search_pair(arr, target - arr[i], i)
    return count

def search_pair(arr, target_sum, first):
    """
    target_sum has arr[i] taken off already
    """
    count = 0
    left, right = first +1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum: #found candidate
            count += right-left
            left += 1
        else:
            right -=1
    
    return count