"""
for self implementations
check out indexed min_d_heap
or min_binary_heap
or min_d_Heap
"""

import heapq

Q = []
Q.append( (distances[s], s))
heapq.heapify(Q)
current_node = heapq.heappop(Q)
heapq.heappush(Q, new_heap_item)