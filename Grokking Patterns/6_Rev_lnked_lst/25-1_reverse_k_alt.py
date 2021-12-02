"""
Given: linked list head, int k
Want: reverse alternating k-sized sublist

just do skipping
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


def reverse_alternate_k_elements(head, k):
  if k <= 1 or head is None:
    return head

  current, previous = head, None
  while current is not None: # break if we've reached the end of the list
    last_node_of_previous_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node

    # reverse 'k' nodes
    i = 0
    while current is not None and i < k:
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

    # connect with the previous part
    if last_node_of_previous_part is not None:
      last_node_of_previous_part.next = previous
    else:
      head = previous

    # connect with the next part
    last_node_of_sub_list.next = current

    # skip 'k' nodes
    i = 0
    while current is not None and i < k:
      previous = current
      current = current.next
      i += 1

  return head