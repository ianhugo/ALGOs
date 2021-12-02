"""
Given: head of singly linked list
Want: reverse list

Strategy:
- iterate through list
- current, prev pointers
- prev = reversed already
- current = the next of the prev

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


def reverse(head):
    previous, current, next = None, head, None
    while current is not None:
        next = current.next  # temporarily store the next node
        current.next = previous  # reverse the current node
        previous = current  # before we move to the next node, point previous to the current node
        current = next  # move on the next node
    return previous