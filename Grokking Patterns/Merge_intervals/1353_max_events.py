"""
not exactly the same but similar idea
Given: array of intervals
Want; possible to attend all, overlaps?

Strategy
- sort
- do merge intervals

"""

"""
O(n lg n) sorting time
O(n) space
"""

def can_attend_all_appointments(intervals):
  intervals.sort(key=lambda x: x[0])
  start, end = 0, 1
  for i in range(1, len(intervals)):
    if intervals[i][start] < intervals[i-1][end]:
      # please note the comparison above, it is "<" and not "<="
      # while merging we needed "<=" comparison, as we will be merging the two
      # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
      # such intervals don't represent conflicting appointments as one starts right
      # after the other
      return False
  return True