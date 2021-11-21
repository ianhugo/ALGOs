"""
Given: array, linkedlist, matrix
Want: find an element

USE: Binary Search

BASIC:
- calculate middle
- decide to search on left or right

1. Normal
- sorted
- but shifted positions
- calculate middle
    - middle = (start + end)/2
    - middle = start + (end - start)/2 (prevent integer overflow)
- compare calcualted middle to middle index
- adjust search frame accordingly
(find ceiling, find next)

2. Circular
- return arr[start % array_length]

3. Infinite
- adjusting (aiiming) the bounds of binary search before start
- compare to target, double each time

4. Bitonic Maximum
- search both sides
- if arr[middle] > arr[middle + 1]
    - descending
    - target = middle, or before middle
    - end = middle
- if arr[middle] < arr[middle+1]
    - ascending
    - target = middle, or after middle
    - start = middle +1
- break when start == end

4.1 Bitonic Search
- find maximum
- then call search on both sides

5 Rotated Array
- calculate middle index 
- arr[start] <= arr[middle] -> ascending sorted
- search the side which might have our key
- if duplicates: do skipping
     - start = start +1
     - end = end -1

6. Find Rotated Minimum
- inflection point
- as it is usually ascending order
- where an element is smaller than its previous index
    - arr[mid] > arr[mid+1] --> mid+1
    - arr[mid -1] > arr[mid] --> mid

6.1 Calcualte Rotations
- find minimum element: 
- find how much moved from index 0
"""