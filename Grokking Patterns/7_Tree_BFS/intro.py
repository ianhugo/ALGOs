"""
When: traverse tree, level by level
Use: Queue
O(w) space
w = max number of nodes on any level

Approaches:

using a queue to traverse
add root, take len, loop based on len

variations:
appending it left or right
processing the items on queue befor einserting

----------------------------------------------
1. Traversal Order
- normal BFS with queue
- append to result array
- append to front (reversed order) or back (normal order)
- alternating at each level?
- operation at each level?
- need to keep track of last node? need conditions? (level order succesor)


-----------------------
2. Minimum root to leaf
- normal BFS with stopping condition




"""