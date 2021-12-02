"""
Given: head of linked list
Want: True if palindrome

Palindrom: values are ascending then descending with same values
1221
1223221

Strategy:
- make ir double linked
- go from front and back

Strategy 2:
- find end of first half
- reverse second half
- determine if palindrom
- restore list

O(n) time
O(1) space
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True

  # find middle of the LinkedList
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next

  head_second_half = reverse(slow)  # reverse the second half
  # store the head of reversed part to revert back later
  copy_head_second_half = head_second_half

  # compare the first and the second half
  while (head is not None and head_second_half is not None):
    if head.value != head_second_half.value:
      break  # not a palindrome

    head = head.next
    head_second_half = head_second_half.next

  reverse(copy_head_second_half)  # revert the reverse of the second half

  if head is None or head_second_half is None:  # if both halves match
    return True

  return False

"""
go through
reverse directions
modify .next
"""
def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev