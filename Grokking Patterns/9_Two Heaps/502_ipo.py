"""
Given:
k = set number of projects
w = set amount of capital
arr[profits] = profits for each project
arr[capital] = capital needed for each project
Only start project, if enough capital
Once start project, profit becomes capital

Want:
maximized capital

Strategy:
- want the maximum of a profit
- want the minimum of a capital invest 
- capital need to be constrained by current capital

- IPQ on both sides
- 


IDEA:

A: find all project we can choose
B: list all projects from A, choose project with max profit

1. add all capitals to min-heap
    - want project with smallest cap requirement
2. iterate through min-heap
    - filter projects, what we can afford
    - insert those profit-projects put into new max-heap
3. select top project of max-heap
4. repeat
"""

"""
Time:
O(n lg n + k lg n) = O(n lg n) 
n = projects
k = number of projects select

Space:
O(n) constant * number of heaps of size n max


FIXED CONSTRAINTS:
number of projects

BEHAVIOR:
initial capital, just an entrance check
keeps it
add profit to it, to qualify for next
"""
from heapq import *

def find_max_cap(capital, profits, num_proj, initial):
    min_cap_heap = []
    max_prof_heap = []

    #insert project capitals to min-heap
    for i in range(0, len(profits)):
        heappush(min_cap_heap, (capital[i], i))
        #put i in for id
    
    available = initial

    for _ in range(num_proj):
        #while non-empty, can afford the top
        # each time initialize a new prof heap
        #but we would want to keep the cap heap all the time
        #find all projects we can afford right now
        #push them all to max heap
        while min_cap_heap and min_cap_heap[0][0] <= available:
            capital, i = heappop(min_cap_heap)
            heappush(max_prof_heap, (-profits[i], i))
        #now all affordable is in max_prof_heap

        #if can't afford any, done
        if not max_prof_heap:
            break
        
        #select project with max profit
        #index 0 has the profit
        available += -heappop(max_prof_heap)[0]
    
    return available