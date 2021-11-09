"""
Given: array of 0s 1s 2s
Want: sort in place

Strategy:
- two pointers
- first pointer = border of 0
- second pointer = border of 1
- iterate through once
- if find 0, put to left, move 1st pointer
- if find 2, put to right, move 2nd pointer
"""

def dutch_flag(arr):
    low, high = 0, len(arr)-1

    i = 0

    while i<= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]

            i+= 1
            low += 1
        elif arr[i] ==1:
            i+= 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    
    return arr