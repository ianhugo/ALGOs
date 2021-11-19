"""
WHEN: 
- reverse links between set of LinkedList nodes
- change order in some manner

Constraint: need to do in place

Approaches:

1. Simple Reversal
- keep track of last
- change pointers

2. Targeted Reversal
- traverse until find
- surgical remove, keep track of pointer connects from both sides
- reverse then udpate
- with skipping? with specific window size?

3. Rotate Linked List
- connect to start
- iterate pointer
"""