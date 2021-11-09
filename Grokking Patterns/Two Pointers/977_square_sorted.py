"""
Given: sorted in non-decreasing array
Want: sorted array of squares

STRATEGY:
- go once through, square everything
- note 0 index
- reverse from start to 0

APPROACH:
- two pointers, 
    start from 0
    or start from each end
- whichever when squared gives larger gets added
"""

def make_squares(arr):
    """
    O(n) space
    O(n) time
    """
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares