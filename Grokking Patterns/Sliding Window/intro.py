"""
When: 
- given array/ linked-list
- find/calculate something among contiguous subarrays
    - or sublists
- of a given size
- or want some kind of subarray

Inefficiency source:
- overlapping of two subarrays
- calculated repeatedly
 
Thought:
- reuse the sum

Visualize:
- sliding window of elements
- subtract element out of window
- add element into window

1. Simple
- set window size
- pop left off
- pop right in

2. Min subarray with target sum/qualities
- pop it in until reach or larger than target
- shrink from left, until reach target again

3. Finding pattern as subarray/substring
- hash map to track
- want length of found pattern = target pattern length
- when greater length, try to shrink


"""