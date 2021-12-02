"""
Given: nums array
Want: bool, is there a cycle of visited indices

Specs:
at each index, move right by x, if positive x
move left by x, if negative x
track indices, to see if cycle
more than one element
O(n) time
O(1) space

Note: 
it is either all positive or all negative

Strategy:
- slow and fast pointers

Question: does it start at same place
only start at index 0?

- just be faster two times
- does it catch up

Checks: faster pointer, checks if sign is still the same
Check if only one element

BUT: need to checck all indices


currently: O(n^2)
as check all element

Observation: if have checked a number
then don't need to check again
keep it as hash
can improve to O(n)

What if mark as 0? or have it as a tuple?

"""


def circular_array_loop_exists(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0  # if we are moving forward or not
    slow, fast = i, i

    # if slow or fast becomes '-1' this means we can't find cycle for this number
    while True:
      # move one step for slow pointer
      slow = find_next_index(arr, is_forward, slow)
      # move one step for fast pointer
      fast = find_next_index(arr, is_forward, fast)
      if (fast != -1):
        # move another step for fast pointer
        fast = find_next_index(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break

    if slow != -1 and slow == fast:
      return True

  return False


def find_next_index(arr, is_forward, current_index):
  direction = arr[current_index] >= 0

  if is_forward != direction:
    return -1  # change in direction, return -1

  next_index = (current_index + arr[current_index]) % len(arr)

  # one element cycle, return -1
  if next_index == current_index:
    next_index = -1

  return next_index