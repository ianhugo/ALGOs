"""
When: cyclic LinkedLists or arrays
How: two pointers different speef

Idea:
two pointers different speed
two pointers will meet, 
if sequence in cyclic loop


----------------------------------------------

1. Simple Cycle
- have two pointers
- one pointer moves 2 at a time
- if meet = cycle


-----------------------

1.1 Simple Middle
- two pointer
- one pointer moves 2 at a time
- when fast pointer reach end, slow = middle


-----------------------

2. Cycle Length
- once meet
- iterate slow again, until meet again
- keep count


-----------------------
3. Cycle Start
- find cycle length k
- 2 pointers, same speed
- place 1 pointer k ahead
- meeting = start


-----------------------
3. Abstracted Cycles (202, 457)
- apply to not just iteration, but any operation done repeatedly
- have one pointer/variable do two ahead


-----------------------
4. Palindrome linked list
- find middle
- reverse second half
- simul iterate
"""