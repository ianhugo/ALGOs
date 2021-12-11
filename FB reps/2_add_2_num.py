"""
GIVEN: two linked list
(reversed representation of an integer)

Want: sum

"""

from collections import ListNode

def solve(self, l1, l2):

    res = ListNode(0)
    res_tail = res
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0) #aiming
        val2 = (l2.val if l2 else 0)

        #computing
        carry, out = divmod(val1+val2+carry, 10)

        #creating new nodes
        res_tail.next = ListNode(out)
        res_tail = res_tail.next

        l1 = (l1.next if l1 else None) #aiming
        l2 = (l2.next if l2 else None)
    
    return res.next
