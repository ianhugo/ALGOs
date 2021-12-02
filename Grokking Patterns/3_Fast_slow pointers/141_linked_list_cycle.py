"""
Given: head of singly linked list
Want: function
- determine if there is cycle
- cycle = circles back
- O(1) space

Strategy:
- need to find a repeated element
- can use two pointers

thought 1:
start at different positions
if cycle, then they will meet

if no loop = will not meet

thought 2:
start one at head
start other at middle
issue: linked list, where is middle? 

thought 3:
staggered start
- pointer 1 go at two jumps
- pointer 2 go at one jumps
- while pointer 1 has not reached a tail
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # found the cycle
    return False