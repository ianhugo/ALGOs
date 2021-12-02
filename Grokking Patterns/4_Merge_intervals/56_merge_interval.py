"""
Given: array of tuple ranges
Want: merged tuple ranges
with no overlaps

Strategy:
- need to sort
- have the cases
- fast and slow pointer
- O(n) time and space

Learned: 
need to sort
simplify cases, with maximizing, minimizing
"""

"""
O(n lg n) time
O(n) space
"""
class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sort the intervals on the start time
  intervals.sort(key=lambda x: x.start)

  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:  # overlapping intervals, adjust the 'end'
      end = max(interval.end, end)
    else:  # non-overlapping interval, add the previous internval and reset
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end

  # add the last interval
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals
