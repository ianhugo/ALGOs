

"""
length of cycle
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            return calculate_cycle_length(slow)

    return 0

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


"""
APPROACH 1
entrance of cycle

previously: determined intersection point of tortoise and hare

Extend: hare has traversed twice as many nodes

F = length not in cycle
a = traversed in cycle
C = length of cycle
n = number of cycle

Hare = 2 * Tortoise
F + nC + a = 2 (F+a)

F + a = nC 
intersection point = number of cycle
F = nC - a
travel from head F = finish cycle starting with a

SO:
start from head pointer
start from intersection pointer

"""

class Solution(object):
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
    
"""
Approach 2:
found linkedlist cycle length
start 2 pointers at head
move 1 pointer ahead by length
keep incrementing until they meet
they will meet at cycle entrance
"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head): #control function
  cycle_length = 0
  # find the LinkedList cycle
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      cycle_length = calculate_cycle_length(slow)
      break
  return find_start(head, cycle_length)


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  # move pointer2 ahead 'cycle_length' nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1