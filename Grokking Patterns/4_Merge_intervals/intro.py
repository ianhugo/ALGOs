"""
When: overlapping intervals
- find overlapping intervals or a "free" interval
- merge intervals if overlap?

6 cases to know

1. no overlap, B ends last
2. no overlap, A ends last
2. A and B overlap, B ends after A
3. A and B overlap, A ends after B
4. A engulfs B
5. B engulfs A


Observation:
when overlap
one of interval's start time lies within the other interval
start = max(a.start, b.start)
end = min(a.end, b.end)


----------------------------------------------
1. Merge Interval 1
- comparing two intervals
- min (starts)
- max (ends)


-----------------------
2. Overlapping Interval (intersection)
- comparing two intervals
- max (starts)
- min (ends)


-----------------------

*: sort intervals?
3. Meeting Rooms / Max Overlapping intervals
- sort
- push to Min heap
- when schedule new, remove all that end before curr_start
- max size of Min heap = max overlapping


-----------------------

4. Common free interval among n sets of intervals
- n sets
- preprocess to have intervals also include identity of set
- each push one to min heap
- dequeue, see if end time before next start time
- if so, found interval
- insert next interval for dequeued id
(add one from each list, each time, then evaluate)


"""