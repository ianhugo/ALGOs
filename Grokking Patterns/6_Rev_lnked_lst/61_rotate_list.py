"""
Given: linked list head
Want: Rotate list to right by k places

Rotate: 
if it was a cycle
push through to the right

Strategy:
go to end of linked list
link to current head
starting from current head, iterate until hit k-th
break off the one before to point to null for next
"""

"""
O(n) time
O(1) space
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  # find the length and the last node of the list
  last_node = head
  list_length = 1
  while last_node.next is not None:
    last_node = last_node.next
    list_length += 1

  last_node.next = head  # connect the last node with the head to make it a circular list
  rotations %= list_length  # no need to do rotations more than the length of the list
  skip_length = list_length - rotations
  last_node_of_rotated_list = head
  for i in range(skip_length - 1):
    last_node_of_rotated_list = last_node_of_rotated_list.next

  # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
  head = last_node_of_rotated_list.next
  last_node_of_rotated_list.next = None
  return head