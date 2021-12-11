"""
Given: array, linkedlist, matrix
Want: find an element

USE: Binary Search

BASIC:
- calculate middle
- decide to search on left or right


----------------------------------------------
0. Normal BST
- sorted array
- check middle
- if smaller, take LHS slice (vice versa)
- check middle again


-----------------------
1. Shifted
- sorted
- but shifted positions
- calculate middle
    - middle = (start + end)/2
    - middle = start + (end - start)/2 (prevent integer overflow)
- compare calcualted middle to middle index
- determine if ascending or descending
- adjust search frame accordingly
(find ceiling, find next)


1.1 Ascending or Descending?
- compare start, middle, end
-----------------------
2. Circular
- return arr[start % array_length]


-----------------------
3. Infinite
- adjusting (aiiming) the bounds of binary search before start
- compare upper bound to target
- if not included double upper each time


-----------------------
4. Bitonic Maximum (find peak) (ascending, then descending)
- search both sides
- if arr[middle] > arr[middle + 1]
    - descending
    - target = middle, or before middle
    - end = middle, continue search
- if arr[middle] < arr[middle+1]
    - ascending
    - target = middle, or after middle
    - start = middle +1, continue search
- break when start == end


-----------------------
4.1 Bitonic Search
- find maximum
- then call search on both sides of max


-----------------------
5 Rotated Array
- calculate middle index 
- arr[start] <= arr[middle] -> ascending sorted
- search the side which might have our key
- if duplicates: do skipping
     - start = start +1
     - end = end -1


-----------------------
6. Find Rotated Minimum
- find middle
- compare middle to start, end (see which part to search)
- inflection point
- as it is usually ascending order
- where an element is smaller than its previous index
- found during search:
    - arr[mid] > arr[mid+1] --> mid+1
    - arr[mid -1] > arr[mid] --> mid


-----------------------
6.1 Calcualte Rotations
- find minimum element
- find how much moved from index 0
"""