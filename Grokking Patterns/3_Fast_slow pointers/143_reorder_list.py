"""
Given: linked list
Want: reordered list
reverse second half
insert in alternate fashion with the start

L0 -> Ln -> L1 -> Ln-1 . . .. 

O(1) space

Strategy:
Find the second half
- use fast-slow pointers find middle
- reverse second half doubly-linked

L0 . . . Lmid -> Lmid + 1 ->  . . . Ln

Insert atlernatively
Issue: when change L0, it will lose reference to L1
- use new attributes

iterate from start
iterate from back
make L0 new next Ln
make Ln new next to L1
and so on

Learned:
clean up solution
think of edge cases

"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  if head is None or head.next is None:
    return

  # find middle of the LinkedList
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  # slow is now pointing to the middle node
  head_second_half = reverse(slow)  # reverse the second half
  head_first_half = head

  # rearrange to produce the LinkedList in the required order
  while head_first_half is not None and head_second_half is not None:
    temp = head_first_half.next
    head_first_half.next = head_second_half
    head_first_half = temp

    temp = head_second_half.next
    head_second_half.next = head_first_half
    head_second_half = temp

  # set the next of the last node to 'None'
  if head_first_half is not None:
    head_first_half.next = None


def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev
