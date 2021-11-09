"""
When: 
- given array/ linked-list
- find/calculate something among contiguous subarrays
    - or sublists
- of a given size

Inefficiency source:
- overlapping of two subarrays
- calculated repeatedly
 
Thought:
- reuse the sum

Visualize:
- sliding window of elements
- subtract element out of window
- add element into window

"""