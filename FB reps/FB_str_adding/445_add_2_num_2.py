"""
Similar to LC 2
but number stored in reverse orer


Given: two linked list
WANT: sum

IDEA 1: reverse the list

"""


"""
IDEA 2:
- do not reverse input
- add through first, do carry as well
- reverse while doing so
- then consider carry (fix carry)
- reverse back and return
"""

def add2(l1, l2):
    n1 = n2 = 0

    cur1, cur2 = l1, l2

    #want LENGTH
    while cur1:
        cur1 = cur1.next
        n1 += 1
    
    while cur2:
        cur2 = cur2.next
        n2 += 1
    

    cur1, cur2 = l1, l2
    head = None

    #normal bits, don't care about carry\
    #reverse while doing so
    while n1 > 0 and n2 >0:
        val = 0

        if n1 >= n2:
            val += cur1.val
            cur1 = cur1.next
            n1 -= 1
        if n1 < n2:
            val += cur2.val
            cur2 = cur2.next
            n2 -= 1
        
        cur = ListNode(val)
        cur.next = head
        head = cur

    #carry bits
    cur1, head = head, None
    carry = 0

    while cur1:

        val = (cur1.val + carry)%10
        carry = (cur1.val + carry)//10

        cur = ListNode(val)
        cur.next = head
        head = cur

        cur1 = cur1.next

    #leftover carry
    if carry:
        cur = ListNode(carry)
        cur.next = head
        head = cur 

    #return as reversed
    return head