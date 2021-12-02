"""

Greedy solution:
start right to left
if can reach then put as True
if not, then False

keep track of the most-left True, left_most
see if at this position (curr_idx + arr[curr_idx] >= left_most)
"""