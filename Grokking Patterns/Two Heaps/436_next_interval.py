"""
Given: array of intervals
Want: next interval start

General idea:
process whole array
find median logic
once get median, start popping things from the max heap
then work on the min heap
last item out of min heap gets -1

next interval of i = j
j has smallest "start" greater than or equal to end of i

APPROACH:
push all into two heaps
max heap 1: sorted by end times
max heap 2: sorted by start times

1: take out top from max end heap = topend
2: findinterval in max start, closest start 
greater than or equal to topend = topstart
3: add topstart to result, as next interval of top end
    - if can't find next interval = -1
4: put top start back
5: repeat until no intervals left in max end
     - keep popping until find next interval for current top end
     


O(n lg n) time
O(n) space
"""

from heapq import *


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  n = len(intervals)

  # heaps for finding the maximum start and end
  maxStartHeap, maxEndHeap = [], []

  result = [0 for x in range(n)]
  for endIndex in range(n):
    heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
    heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))

  # go through all the intervals to find each interval's next interval
  for _ in range(n):
    # let's find the next interval of the interval which has the highest 'end'
    topEnd, endIndex = heappop(maxEndHeap)
    result[endIndex] = -1  # defaults to - 1
    if -maxStartHeap[0][0] >= -topEnd:  #if start after curr top end
      topStart, startIndex = heappop(maxStartHeap)
      # find the the interval that has the closest 'start'
      while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:    #get to closest start
        topStart, startIndex = heappop(maxStartHeap)
      result[endIndex] = startIndex
      # put the interval back as it could be the next interval of other intervals
      heappush(maxStartHeap, (topStart, startIndex))
      #discard others, as they have an even higher start
      #next end will have a lower end, so others are useless

  return result