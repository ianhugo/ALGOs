"""
Given: arr of intervals
Want; min # rooms required

Observation:
if conflict between two = need two rooms
if conflict between three = need three rooms . . .

Strategy:
- iterate through
- keep track of curr_end vs next_start

Learned:
- need to sort anyway
- can use data structs
- don't be obsessed with time and space, to create wrong implements
- make sure logic works first

Example:
Schedule m1 in r1
Schedule m2 in r2
Schedule m3 in which room?  = need to know which ends first

NEED:
sorting
keep track of mutual exclusivity
keep track of ending time of all meetings happening
= use a min heap

Heap use:
- add to min-heap
- when put in m_k
- remove all meetings ended before m_k
- add m_k
- heap has all overlapping meetings
- use counter to remember max size of heap = min rooms needed

"""

"""
Simialr problems:
Find maximum overlap
Train platforms needed
"""

"""
O (n lg n) sorting
O(lg n) for each heap operation

O(n) space
"""
from heapq import *

#create these classes before starting
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        #implementing this allows heap
        return self.end < other.end

def min_meet_rm(meetings):

    meetings.sort(key = lambda x: x.start)

    minRooms = 0
    minHeap = []

    for meeting in meetings:
        
        #removing meetings by start time
        #while there are meetings
        #remove meetings with end times before this meeting's start
        while (len(minHeap)> 0 and meeting.start >= minHeap[0].end):
            heappop(minHeap)
        
        #add to min heap
        heappush(minHeap, meeting)

        #tracking
        minRooms = max(minRooms, len(minHeap))
    
    return minRooms
