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

-----------------------------------
1. Simple (643, )
- set window size
- pop left off
- pop right in

-----------------------
2. Min subarray with target sum/qualities (340, 904, 3, 424)
- pop it in until reach or larger than target
- or reach a constraint
- shrink from left, until reach target/constraint again
- constraint can be tracked with a hash map (distinct k elements)


------------------------
3. Finding pattern as subarray/substring (76, 567, 438, 30)
- given input and pattern/constraint
- iterate through with hash map
- iterate through input, when matched, increment matched variable, decrement hashmap
- want length of found pattern = target pattern length
- when greater length, try to shrink
- with shrinking, decrement matched variable, re-increment hashmap


"""