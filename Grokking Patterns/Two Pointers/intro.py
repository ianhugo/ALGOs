"""
When:
- sorted arrays/ linked list
- find set of elements, with constraints
- set = pair, trip, subarray

Sample:
given sorted array, find a pair, which sum equal to target

Brute:
consider each, loop through each

Two-Poitner Strategy:
- start at both ends
- if curr_sum is too big, move end pointer
- if curr_sum is too small, move start pointer
- O(n)

"""