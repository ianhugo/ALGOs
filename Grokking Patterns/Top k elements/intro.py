"""
When: find top/small/frequent/characteristic K elements among array

USE: Heap

Approaches:

1. Top K:
- k sized min heap
- iterate through add k numbers
- for each new, if larger than current top
- pop top, add new

1.1: Lowest K:
- use max heap

1.2: K-closest to xxx:
- can use any operation to determine min-heap/max-heap

1.3: applied
- want K closest in some form
- "minimum cost"

1.4: modified nodes
- add new attributes, use that to heapify

2. Top K based on x:
- find that x/closest first, binary search
- if sorted array, closest candidates are adjacnet K on both sides

3. Repeated elements, not used consecutively
- keep node outside
- delayed putting back into heap

4. Repeated elements, used K apart
- keeping every node out for K time
- use queue
- when queue hit k length, put back

5. Top K Frequency in a stream:
- keep hash map
- keep popping in
- it is already O(n)


Observation:
Be careful deciding to use max or min heap
are we trying to keep smaller ones? choose max
push if smaller than curr_top

are we trying to keep bigger ones? choose min
push if larger than curr_top
"""


"""
Drafts:

Max distinct elements:
given K
iterate through, push all into hash
psuh all into max heap, max by frequency
take out K, then keep popping, until unique frequency
(if use min heap, might be faster)

Sum of elements:
build max heap of size k2
iterate through
pop first, then start summing



"""