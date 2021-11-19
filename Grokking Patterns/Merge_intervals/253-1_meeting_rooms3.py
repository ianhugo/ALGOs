"""
Given: arr of intervals, int k of rooms available
Want; arr of bools, which meetings can be schedules

same as previous
before heappush, check length
if exceed, then it is false

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


        #ADD CONDITIONAL HERE
        #add to min heap
        heappush(minHeap, meeting)

        #tracking
        minRooms = max(minRooms, len(minHeap))
    
    return minRooms
