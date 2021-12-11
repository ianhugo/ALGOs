"""
Given: array, weights
WANT: function, that returns index, based on weights

IDEA:
- use prefix sum, to beef up weights
- so can do searching
- use cumulative sum to reflect probability weights

"""

import random

class Solution:
    def __init__(self, w):
        self.pref_sum = []
        sumd = 0

        for weight in w:
            sumd += weight
            self.pref_sum.append(sumd)
        
        self.tot = sumd
    
    def pick(self):

        target = self.tot * random.random()

        low, high = 0, len(self.pref_sum)

        while low<high:
            mid = low + (high-low)//2

            if target > self.pref_sum[mid]:
                low = mid +1
            else:
                high = mid
        
        return low
