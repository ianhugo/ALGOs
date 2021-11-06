"""
(https://www.youtube.com/watch?v=_dlzWEJoU7I)
strategic hybrid of
binary isnertion sort + merge sort

insertion sort: go through all items, then move it back to the correct position
binary insertion sort: find correct position by using binary search on the sorted bit
(https://www.youtube.com/watch?v=-OVB5pOZJug)

1: are there more than 64 elements?
Yes = binary insertion sort
No = deploy more sophisticationn

2: identify a run
some data that is already in the data
(in some increasing sequence, can have gaps)

3: determine min run
min-run = minimum length of each run
that gives most efficient time later on

4: now create runs of min-runs
use binary insertion to sort the min-runs

5: if min run is met immediately
the next element is also included

6: if descending order (not descending and equal)
flip into ascending order

7: Merge sorted runs

8: acceleration when merging
say put down one element from run_a, run_a[x]
now take run_a[x] and run_a[x+1] as a range
go through run_b, add all that are within this range
once hit 7 of these
take run_a[x+1], try to find it in run_b
directly copy more
then return to merge sorting as normal

better than binary insertion sort after 64
better than merge sort as it does runs and accelerations

"""