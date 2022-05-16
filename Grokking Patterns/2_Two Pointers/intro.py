"""
When:
- sorted arrays/ linked list
- find set of elements, with constraints
- set = pair, trip, subarray
- identify two members

Sample:
given sorted array, find a pair, which sum equal to target

Brute:
consider each, loop through each

Two-Poitner Strategy:
- start at both ends
- if curr_sum is too big, move end pointer
- if curr_sum is too small, move start pointer
- O(n)

-----------------------------------------------

1. Target Sum (2sum)
- sorted array
- start from front, start from back
- if summed too big, move back pointer
- if summed too small, move front pointer


-----------------------

2. Duplicates
- one pointer = barrier
- one pointer = iterator
- when find unique, move barrier, do switchies
- iterator keeps going


-----------------------

3. Want square sorted array
- find zero
- iterate backwards for negatives
- iterate forwards for non-negatives
- "merge" into new array


-----------------------

4. Target Trip Sum (3sum)
- sort it
- iterate through
- for each position, spawn a 2 sum for arr[i+1:]


-----------------------

5. Find continuous subarray with product less than target (713)
- iterate through
- when hit or larger than product
- shrink until just smaller
- use queue, to append all permutation of subarray (as they are all smaller)


-----------------------

6. Target Quad Sum (4 sum)
- for loops to choose each
- for each, choose another to make a pair
- then for each pair do 2sum


-----------------------
7. minimum subarray to sort (581)
(use two pointers and shrinking)
- from left: find first that is smaller than prev
- from right: find first that is larger than prev
- find max, min of window
- extend left to include all bigger than min
- extend right to include all smaller than max
"""