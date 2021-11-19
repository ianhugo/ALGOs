"""
Given: two lists of intervals
Want: itnersection of interval lists

Strategy:
- iterate through each
- find intersections
- if not finished whole block, retain that for next cycle
- two pointers for which element at for each list
- use while loop

Observation:
when overlap
one of interval's start time lies within the other interval
start = max(a.start, b.start)
end = min(a.end, b.end)
"""

#this looks cool

"""
O(m++n) time
m, n = length of intervals

O(k) space for length of results space

"""
def merge(intervals_a, intervals_b):
  result = []
  i, j, start, end = 0, 0, 0, 1

  while i < len(intervals_a) and j < len(intervals_b):
    # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
    a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                   intervals_a[i][start] <= intervals_b[j][end]

    # check if intervals overlap and intervals_a[j]'s start time lies within the other intervals_b[i]
    b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                   intervals_b[j][start] <= intervals_a[i][end]

    # store the the intersection part
    if (a_overlaps_b or b_overlaps_a):
      result.append([max(intervals_a[i][start], intervals_b[j][start]), min(
        intervals_a[i][end], intervals_b[j][end])])

    # move next from the interval which is finishing first
    if intervals_a[i][end] < intervals_b[j][end]:
      i += 1
    else:
      j += 1

  return result