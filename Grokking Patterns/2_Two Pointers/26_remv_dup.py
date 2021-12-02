"""
GIVEN: sorted array numbers
Want: remove all duplicates, return new length
Res: no extra space

STRATEGY:
- two pointers
- lagged pointers, pt1, pt2
- both start at start
- if unique, pt1 stay
- increment pt2
- if duplicate, move pt1 up
- increment pt2
- if new, pt1 stay
- pt2 move
- now start taking slices

LEARNED:
just switch, no need to do slices
"""

def remove_dup(arr):
    """
    two pointers
    "quicksort-ish"
    if unique
    put nondup into left side
    guardian pointer at +1 index

    O(n) time
    O(1) space
    
    """
    next_non_dup = 1

    i = 1

    while (i < len(arr)):
        if arr[next_non_dup -1] != arr[i]: #if unique
            arr[next_non_dup] = arr[i]
            next_non_dup +=1
        i+= 1
    
    return next_non_dup
