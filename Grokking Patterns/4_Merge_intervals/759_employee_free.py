"""
Given: arr of arrs intervals
Want: intervals which are not scheduled for all members of arr

Strategy:

Enter:
there are multiple arrays of intervals
[[a1, a2], [a3, a4]]
[[b1, b2]. [b3, b4]]
...

BRUTE:
go through each time
then see if we can merge, merge to big arr
after that find gaps in the merged
O(n * m)
m = number of employees

Thought: is there a way not to check all of them?
This is O(maxlen*k)

LEARNED:
use heaps
- take first interval -> min heap
- min heap = interval with smallest start
- compare with next smallest start, find gaps

KEY OBSERVATION:
- use minheap to do sorting of one layer (one subset of things)
- abstract the characteristic of the gap: between current_end, next_start

"""


"""
O(n lg k) time
lg k for heaps

O(k) space, heap biggest if k size
"""

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        self.employeeIndex = employeeIndex #index of employee in big list
        self.intervalIndex = intervalIndex  # current idx of interval in employee's

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))
        #create as an employee interval
        #heap is size K
    
    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        
        #if prev Interval, not overlapping with next
        #append a result
        if previousInterval.end < queueTop.interval.start:
            
            #append result
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            
            #switch places
            previousInterval = queueTop.interval

        else: #overlap, update interval
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval
    

        #add employee next interval
        #locate the popped interval's employee idx
        employeeSchedule = schedule[queueTop.employeeIndex]

        #check if reached end of this employee's schedule
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            #create new employee interval
            #increment 1 across the board
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))