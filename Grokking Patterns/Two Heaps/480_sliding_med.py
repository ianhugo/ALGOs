"""
Given: array of numbers, int k
Want: median of all k sized sub-arrays


Strategy:
(not sliding window, as this is median)
- iterate over
- maintain two indexed heaps
-- removals is expensive

"""