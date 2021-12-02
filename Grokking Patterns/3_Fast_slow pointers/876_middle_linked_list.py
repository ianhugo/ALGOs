"""
Given: linked list
Want: middle

Strategy:
- fast and slow pointers
- check if linked list has cycle
A: no cycle
- link end to start
- fast and slow, meeting point = middle
B: yes cycle
- find cycle entrance point, detach
- take node before entrance to be end
- make cycle

Edga Case:
even/odd

O(n) time
O(1) space

Learned:
think more carefully
if twice as fast
fast pointer reach end
slow pointer at middle

"""

def find_middle_of_linked_list(head):
    """
    O(n) time
    O(1) space
    """
  slow = head
  fast = head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next
  return slow
