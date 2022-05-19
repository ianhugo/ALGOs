

"""
max k length continuous substring
"""
def longest_k_distinct(str1, k):

    window_start = 0
    max_len = 0
    char_freq = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char]+= 1

        while len(char_freq)> k:
            left_char = str1[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1
        
        max_len = max(max_len, window_end-window_start+1)
    
    return max_len


"""
does string contain permutaiton of the given pattern
"""

def find_permute(str1, pattern):

    wind_start, matched = 0,0
    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    
    for wind_end in range(len(str1)):
        right_char = str1[wind_end]
        if right_char in char_freq:
            char_freq[right_char]-=1
            if char_freq[right_char] ==0:
                matched += 1
        
        if matched == len(char_freq):
            return True
        
        if (wind_end - wind_start +1) >= (len(pattern)-1):
            left_char = str1[wind_start]
            wind_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                
                char_freq[left_char] += 1
    
    return False

"""
two pointers: 3sum
"""


def search_trips(arr):

    arr.sort()
    trips = []
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
    search_pair(arr, -arr[i], i+1, trips)   #for each find its complements as 2 sum

def search_pair(arr, target, left, trips):
    right = len(arr)-1

    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target:
            trips.append([-target, arr[left], arr[right]])
            left += 1
            right -=1

            #skip duplicates
            while left<right and arr[left] == arr[left-1]:
                left += 1
            while left<right and arr[right] == arr[right+1]:
                right -= 1
        elif target > cur_sum:
            left += 1
        else:
            right -=1


"""
Given array of intervals
minimum number of rooms required
"""

from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end < other.end

def min_meet_rm(meetings):

    meetings.sort(key = lambda x: x.start)

    minRooms = 0
    minHeap = []

    for meeting in meetings:
        
        #pre-state, target-state, post-state
        while (len(minHeap)>0 and meeting.start >= minHeap[0].end):
            heappop(minHeap)
        
        heappush(minHeap, meeting)  #isolate meetings that have not ended, when this meeting starts

        minRooms = max(minRooms, len(minHeap))

    return minRooms


"""
Cyclic sort; find missing
"""

def find_missing(nums):

    i, n = 0, len(nums)

    while i<n:
        j = nums[i]

        #if within range, number not already in place (duplicated)
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n

"""
Tree DFS
given: tree
want: number of paths, where sum == target
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def count_paths(root, S):
    return count_paths_recur(root, S, [])

def count_paths_recur(curr, S, curr_path):

    if curr is None:
        return 0
    
    curr_path.append(curr.val)
    path_count, path_sum = 0, 0

    for i in range(len(curr_path)-1, -1, -1):
        path_sum += curr_path[i]
        if path_sum == S:
            path_count += 1
    
    path_count += count_paths_recur(curr.left, S, curr_path)
    path_count += count_paths_recur(curr.right, S, curr_path)

    del curr_path[-1]

    return path_count

"""
Two Heaps
Optimization
maximized profits
"""

from heapq import *

def find_max_cap(capital, profits, num_proj, initial):
    min_cap_heap = []
    max_prof_heap = []

    for i in range(0, len(profits)):
        heappush(min_cap_heap, (capital[i], i))
    
    available = initial

    for _ in range(num_proj):

        while min_cap_heap and min_cap_heap[0][0] <= available:
            capital, i = heappop(min_cap_heap)
            heappush(max_prof_heap, (-profits[i], i))
        
        if not max_prof_heap:
            break
            
        available += -heappop(max_prof_heap)[0]
    
    return available


"""Top Sort
"""


class Solution:
    White = 1
    Gray =  2
    Black = 3

    def find_order(self, num, pre):

        adj_list = {}

        for src, dest in pre:
            adj_list[src].append(dest)

        top_sort = []
        is_possible = True

        color = {k: Solution.White for k in range(num)}

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return
            
            color[node] = Solution.Gray

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.White:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.Gray
                        is_possible = False
                
                color[node] = Solution.Black
                top_sort.append(node)
        
        for vertex in range(num):
            if color[vertex] == Solution.White:
                dfs(vertex)
        
        return top_sort[::-1] if is_possible else []
        