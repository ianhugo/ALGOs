"""
When: a list of sorted arrays (k of them)
What: push smallest element from each to heap
then push more according to which was popeed

Trick 1: keep track of largest number inserted into heap
for ranges

Trick 2:
use the heap to store K elements
if want kth max ones
use a min heap 
insert pairs larger than top
pop top

"""