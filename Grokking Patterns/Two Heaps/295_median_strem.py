"""
Given: number stream
Want: dynamically return the median


IDEA:
Observation 1: direct access to median helps
Observation 2: fast way to insert numbers
Observation 3: don't need full sorted

max-heap: store smaller half of input numbers
min-heap: store larger half of input numbers

median values = calculation between top of both heaps

1: heaps are balance, or 1 off
2: max heap = smaller numbers, min heap = larger numbers
    - max-heap numbers <= top of max heap
    - min-heap numbers >= top of min heap
3: balancing heaps
    - big max heap: remove largest element, give to min heap
    - big min heap: remove smallest element, give to max heap
4: insertion based on comparison with current tops
    - if smaller than maxheap top = insert in max heap
    - if larger than minheap top = isnert in min heap

Note:
- python heap is a minheap
- so if want maxheap, push in negatives

Note:
- need to reolsve odd numbered
- so preference for maxheap having one more
- middle if odd, is on the maxheap
"""

"""
Alternate: use AVL trees
if odd: root = median
if even: consecutive elements, including root

keep track of two pointers
"""


"""
O(lg n) = insertion to heap
O(n) space
"""
from heapq import *


class MedianOfAStream:

    def __init__(self):
        maxHeap = []    #smaller nums
        minHeap = []    #bigger nums

    def insert_num(self, num):
        
        #where to insert
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        #balancing, equal or one off
        #prefer maxHeap have one more
        if len(self.maxHeap) > len(self.minHeap) +1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap < len(self.minHeap)):
            heappush(self.maxHeap, -heappop(self.minHeap))


    def find_median(self):
        
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2.0 + self.minHeap[0]/2.0

        return -self.maxHeap[0]/1.0