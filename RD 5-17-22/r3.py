


def binary_search(arr, target):

    l, r = 0, len(arr) - 1
    while l + 1 < r:
        mid = 1 + (r - l) // 2 #floor division
        
        if arr[mid] < target:
            l = mid
        else:
            r = mid
    
    if abs(target - arr[l]) <= abs(target - arr[r]):
        return l
    else:
        return r

"""
Tree Properties

1: nodes in a balanced tree
height = x
branch per node = y
nodes = y^x
(for each node, y, for each of those nodes y
so y * y, y * y * y . . .)

2: height of tree in a balance tree
height = log_(branches) nodes


"""
from collections import deque

def bfs(tree):
    visited = [False]*tree.nodes
    prev = [False]*tree.nodes
    queue = deque()
    queue.append(0)
    visited[0] = True

    while not len(queue) == 0:
        node = queue.popleft()
        neighbors = tree[node].neighbors

        for next in neighbors:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                prev[next] = node
    
    return prev

# count number of nodes
# can do some other operations
def dfs(graph, start, n):

    count = 0
    visited = [False] * n
    stack = deque()
    stack.append(start)
    visited[start] = True

    while len(stack) != 0:
        node = stack.pop()
        count += 1
        edges = graph[node].edges

        if edges != []:
            for edge in edges:
                if not visited[edge.to]:
                    stack.append(edge.to)
                    visited[edge.to] = True
    

    return count

"""
Backtracking:
doing a DFS on a deciion tree
need to model problem as a decision tree
O(b^d)
b = branching factor
d = depth

decision tree: 
- make a sequence of decisions
- build up partial solutions
- reach full solution

root = "empty" partial solution
leaves = full solution

Knight's Tour
1: Feasibility (find one knight tour)
2: Enumeration (find all knight tour)
3: Counting (how many knight tours)
4: Optimization (knight tour with fewest crossing)

N-Queens
Partial solution:   a board with 0 to n queens
Root:       empty board
Children:   where to place next queen on next row
Leaves:     board with n queens
Dead Ends:  boards where two queens attack each other

Sudoku:
Nodes:      partially filled board
Root:       only given numbers
Children:   what digit to put in next cell
Leaves:     completely filled board
Dead ends:  boards with conflict
Iteration:  fill cells from top left, to bottom-right
(have to have traversal checking code)

Parenthese balanccing:
Nodes:      partially balanced parantheses
Root:       empty string
Children:   add ( or )
Leaves:     balanced paranthese string of size  n
Dead ends:  unbalanced 
            1: left parentheses open
            2: closed an unopened parentheses
Iteration:  put parenthese in next position

"""


def backtrack(partial):
    if dead_end(partial):
        prune()
        return
    
    if is_full(partial): #leave/full solution
        processing()
        print(partial)
    else:   #continue going
        for child in children(partial):
            backtrack(child)

"""
Subsets
= binary decision for each element

Root:       no decisions yet
Children:   take or not take this element
Leaves:     made decision on all elements
Dead ends:  no dead ends
Iterations: are we putting this element or not (each level)

O(2^n)

"""

def subset(L):
    backtracking([], 0, L)

def backtracking(picked, i, L):
    if i == len(L):
        print(picked)
    else:
        backtracking(picked+[L[i]], i+1, L)
        backtracking(picked, i+1, L)

"""
Permutations
Root:       empty list
Children:   what element to put next
Leaves:     every element in the list
Dead Ends:  none
Iterations: each level, add sth new

O(n!)
(N-queens, TSP . .. )
"""


def permutations(nums):
    backtracking([], nums)

def backtracking(perm, nums):
    if len(perm) == len(nums):
        print(perm)
        return
    
    for num in nums:
        if not num in perm:
            backtracking(perm[num], nums)

"""
Optimizations:
1: represent partial solution smaller
2: store extra state, avoid recomputation
3: copy vs inplace

"""


"""
Dynamic Programming
1: Optimal substructure
optimal solution = optimal subproblems summed

2: Overlapping subproblem
subproblems repeated

similar to backtracking
but mapping to subproblem space instead
(have to pass parameters for targeting subproblem space)
(because have to store/reference the solution)

WHAT IS DP?
try all solutions
cache solutions

1: Top-Down
recurrence
(base case, passing down variables)

2: Bottom-up
use a matrix
(padding)


STEPS:
1. Analyze Recursion Tree
2. Brute Force
3. Cache Optimal States
    - add memo as argument
    - check for answers
    - store answers before return

Preprocessing   (base cases, pruning)
Processing      (spawn workers)
Postprocessing  (on return)

Preprocessing
Check Solutions (another base case, return immed)
Processing
Cache Solutions (after workers returned)
Postprocessing

"""



"""
Dynamic Programming: Bottom-up

to note:
1: index manipualtion
2: initialize DP table
3: pad base cases
4: build general cases
5: result in last cell
6: reconstruct soluution
"""

# Pathrise review complete
###############################################################



"""
Dikstra
Single source shortest path

0: have a visited array, a previous array, a distance array
1: start from a source
2: loop through edges
3: with edge x, compute new distance to node b, add in distance to current node 
4: if new distance, smaller than distance recorded in distance array, change
5: after looping, choose the lightest edge
6: repeat

no negative edges
because it closes edges/nodes
"""

import math

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value #current lowest distnace value to reach this node


def dijkstra(start, end, adj):
    n = len(adj)

    dist = [math.inf] * n
    dist[start] = 0
    visited = [False] * n
    prev = [None] * n

    pq = deque()

    pq.append(Node(start, 0))

    while len(pq) != 0:
        node = pq.popleft()
        visited[node.id] = True

        if dist[node.id] < node.value:
            continue #node has been processed begtter

        for edge in adj[node.id]:
            if visited[edge.to]:
                continue
                
            new_dist = dist[node.id] + edge.cost

            if new_dist < dist[edge.to]:

                prev[edge.to] = node.id
                dist[edge.to] = new_dist

                pq.append(Node(edge.to, dist[edge.to]))
            
            if node.id == end:
                return dist[end], prev
    
    return math.inf, prev

"""
Bellman Ford
iterate V-1 times
update along all edges
can do negative edges, but no negative cycles
"""

def bellman(graph, v , start):

    dist =  [math.inf * v]
    dist[start] = 0
    prev = [None * v]

    for i in range(v-1):
        for edges in graph:
            for edge in edges:

                if dist[edge.pre] + edge.cost < dist[edge.to]:
                    dist[edge.to] = dist[edge.pre] + edge.cost
                    prev[edge.to] = edge.pre
    
    return prev


# prelims done
###############################################################

"""
Sliding Window

a window that moves
with tracking variables
maybe a tracking hashmap

iterate through window_end or window_start

"""


"""
424
Given: string lowercase, int k
Want: 
longest substring with same letter
can replace k characters

1: start at x
2: expand, replace characters count
3: when hit limit, store max
4: shrink 
"""


def length_longest_substring(str1, k):

    wind_start, max_len, max_repeat = 0, 0, 0

    freq_map = {}

    # extending the range
    for wind_end in range(len(str1)):
        
        # range extended
        right_char = str1[wind_end]

        # add extended char into map
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] += 1

        # find char that is most repeated
        max_repeat = max(max_repeat, freq_map[right_char])

        # check if after subtractions, over limit of repeated capacity
        # this computes how many letters to replace
        if (wind_end - wind_start + 1 - max_repeat) > k:

            #if so pop the left_char
            left_char = str1[wind_start]
            freq_map[left_char] -= 1
            wind_start += 1
        
        # measure max length now, and store
        max_len = max(max_len, wind_end - wind_start + 1)
    
    return max_len

"""
Want: max k distinct, longest string
"""

def distinct_substring(str1):

    wind_start = 0
    max_len = 0
    char_index = {}

    for wind_end in range(len(str1)):

        right_char = str1[wind_end]

        # is it distinct
        if right_char in char_index:

            # if not, then find new wind_start
            wind_start = max(wind_start, char_index[right_char])

        # update char_index
        char_index[right_char] = wind_end

        max_len = max(max_len, wind_end - wind_start + 1)
    
    return max_len

"""
30
Given: string, list of words
Want:
indices of substrings
substring = include all given words
words are same length
"""

def find_words_concat(str1, words):

    if len(words) == 0 or len(words[0]) == 0:
        return []
    
    word_freq = {}

    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
    results_indices = []
    words_count = len(words) # how many are we looking for
    word_length = len(words[0])

    # managing which indices to start
    for i in range((len(str1 - words_count * word_length) + 1)):
        words_seen = {}

        for j in range(0, words_count):

            next_word_idx = i + j * word_length

            word = str1[next_word_idx: next_word_idx + word_length]

            #if invalid word
            if word not in word_freq:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            #if more than needed
            if words_seen[word] > word_freq.get(word, 0):
                break

            if (j + 1) == words_count:
                results_indices.append(i)
    
    return results_indices


"""
Two Pointers

"""

"""
3 sum
"""

def search_trips(arr):
    arr.sort()
    trips = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        search_pair(arr, -arr[i], i+1, trips)
    
    return trips

def search_pair(arr, target, left, trips):
    right = len(arr) - 1

    while left < right:
        cur_sum = arr[left] + arr[right]

        if cur_sum == target:
            trips.append((-target, arr[left], arr[right]))
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif target > cur_sum:
            left += 1
        else:
            right -= 1

"""
Subarray product
more like sliding window
"""

def find_subarr(arr, target):

    result = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        while (product >= target and left < len(arr)):

            product /= arr[left]
            left += 1
        
        temp_list = deque()

        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    
    return result

"""
Shortest sort subarray

find the out of place one
on the min side and the max side
then find max and min in this window
extend until covers other in the original array
"""

def shortest_sort(arr):

    low, high = 0, len(arr) -1

    while (low < len(arr)-1 and arr[low] <= arr[low+1]):
        low += 1
    
    if low == len(arr) -1:  #iterated to the back, it is sorted
        return 0

    while (high > 0 and arr[high] >= arr[high-1]):
        high -= 1
    
    sub_max = -math.inf
    sub_min = math.inf

    for k in range(low, high + 1):
        sub_max = max(sub_max, arr[k])
        sub_min = min(sub_min, arr[k])
    
    #extend subarray
    #extend in this way, because already checked it is uphill
    while (low > 0 and arr[low-1] > sub_min):
        low -= 1
    
    while (high < len(arr)-1 and arr[high+1] < sub_max):
        high += 1
    
    return high - low + 1

"""
Fast and Slow Pointers
"""

def find_cycle_start(head):
    cycle_length = 0

    slow, fast = head, head

    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

def find_start(head, cycle_length):
    pt1 = head
    pt2 = head

    #move pointer ahead by cycle length
    while cycle_length > 0:
        pt2 = pt2.next
        cycle_length -= 1
    
    #wait to meet again
    while pt1 != pt2:
        pt1 = pt1.next
        pt2 = pt2. next
    
    return pt1

"""
abstracted cycle"""

def circular_loop(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast, = i, i
    
        while True:
            slow = find_next_idx(arr, is_forward, slow)
            fast = find_next_idx(arr, is_forward, fast)

            if (fast != -1):
                fast = find_next_idx(arr, is_forward, fast)
            
            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True
    return False

def find_next_idx(arr, is_forward, curr_idx):
    direction = arr[curr_idx] >= 0

    if is_forward != direction:
        return -1   #change in direction
    
    next_idx = (curr_idx + arr[curr_idx]) % len(arr)

    if next_idx == curr_idx:
        next_idx = -1
    return next_idx

"""
Merge Interval: 
use conditionals
use heap
"""

"""
Cyclic Sort
"""

# VANILLA

def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1 # indexing adjust
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:   # stay here until it is placed correctly
            i += 1
    return nums

def find_missing(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]

        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else: # placed correctly move on, out of range move on
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n


    """
    want kth missing number
    """

def find_kth(nums, k):
    n = len(nums)
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missing_nums = []
    extra_nums = set()

    for i in range(n):
        if len(missing_nums) < k:
            if nums[i] != i + 1: #adjusted idx check
                missing_nums.append(i+1)    #this idx wrong, need pos number
                extra_nums.add(nums[i])     #this is extra, keep it for later
    
    # now do we have enough k numbers?
    # if not, then add more, by going beyond length
    # but need to check if the extra nums has it
    # if it is, then we are not missing it

    i = 1
    while len(missing_nums) < k:
        candidate = i + n

        if candidate not in extra_nums:
            missing_nums.append(candidate)
            i += 1

    return missing_nums

"""
Tree DFS
"""


def has_path(root, sum):

    if root is None:
        return False
    
    if root.val == sum and root.left is None and root.right is None:
        return True
    
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)



def find_paths(root, required_sum):
    all_paths = []
    find_paths_recur(root, required_sum, [], all_paths)

    return all_paths

def find_paths_recur(curr, required_sum, curr_path, all_paths):

    if curr is None:
        return
    
    # root to leaf restriction
    if curr.val == required_sum and curr.left is None and curr.right is None:
        all_paths.append(list(curr_path))
    else:
        find_paths_recur(curr.left, required_sum-curr.val, curr_path, all_paths)
        find_paths_recur(curr.right, required_sum-curr.val, curr_path, all_paths)
    
    del curr_path[-1]


"""
count number of paths that get to sum, not root to leaf
"""


def count_paths_recur(curr, S, curr_path):

    if curr is None:
        return 0
    
    curr_path.append(curr.val)
    path_count, path_sum = 0, 0

    # backwards at each node
    # will include every permutation
    for i in range(len(curr_path)-1, -1, -1):
        path_sum += curr_path[i]

        if path_sum == S:
            path_count += 1
    
    path_count += count_paths_recur(curr.left, S, curr_path)
    path_count += count_paths_recur(curr.right, S, curr_path)

    del curr_path[-1]

    return path_count
    
"""
Tree diameter: longest path between two leafs
"""

def recur_diameter(curr):

    if curr == None: #sentry
        return 0
    
    len1 = recur_diameter(curr.left)
    len2 = recur_diameter(curr.right)

    tree_diameter = max(tree_diameter, (len1 + len2 + 1))

    len = max(len1, len2)

    return len+1 


"""
Two Heaps
"""

"""
min heap, max heap
checking, if needed, balancing
"""

from heapq import heappush, heappop

class median:
    def __init__(self):
        max = []
        min = []
    
    def insert_num(self, num):

        if not self.max or -self.max[0] >= num:
            heappush(self.max, -num)
        else:
            heappush(self.min, num)
        
        if len(self.max) > len(self.min) + 1:
            heappush(self.min, -heappop(self.max))
        elif len(self.min) > len(self.max) + 1:
            heappush(self.max, -heappop(self.min))
    
    def find_med(self):
        if len(self.max == len(self.min)):
            return -self.max[0]/2.0 + self.min[0]/2.0
        
        return -self.max[0]/1.0

"""constraints two heap
"""

def find_max(cap, prof, num, initial):

    min = []
    max = []

    for i in range(0, len(prof)):
        heappush(min, (cap[i], i))

    available = initial

    for _ in range(num):

        # add while you can afford
        while min and min[0][0] <= available:
            capital, i = heappop(min)
            heappush(max, (-prof[i], i))
        
        if not max:
            break
        
        # choose the best
        available += -heappop(max)[0]

    return available

"""
Subset = 
decision tree
to put or not to put here

Permutation =
put in which position here
"""

"""Bit manipulation version of subsets"""
def subsets(nums):
	result = []
	n = len(nums)
	
	#number of subsets
	size = math.pow(2, n) 
	

	for i in range(size):
		val = []
		for j in range(n):
			if (i & (1<< j) != 0):
				val.append(nums[j])
		result.append(val)

	return result


"""
Evaluating Expression in different ways
divide and conquer
can use memoization
"""

def evaluate(input):

    res = []
    
    #input is just a number
    if "+" not in input and "-" not in input and "*" not in input:
        res.append(int(input))
    else:
        for i in range(0, len(input)):
            char = input[i]

            if not char.isdigit():
                #divide and conquer here
                #sort of determining there are two parenthese
                #separating these parts here
                left = evaluate(input[0:i])
                right = evaluate(input[i+1:])
                for part1 in left:
                    for part2 in right:
                        if char == "+":
                            res.append(part1 + part2)
                        elif char ==  "-":
                            res.append(part1 - part2)
                        elif char ==  "*":
                            res.append(part1 * part2)


"""Unique Binary Trees
Given: number n
Want; return structurally unique BST
build from ground up
"""

def find_recur(start, end):
    res = []

    #empty subtree
    if start > end:
        res.append(None)
        return res
    
    #starting at different idx
    for i in range(start, end+1):
        #building diff trees
        left = find_recur(start, i-1)
        right = find_recur(i+1, end)

        #appending different versions to curr node
        for left_tree in left:
            for right_tree in right:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                res.append(root)
    
    return res


"""
Modified Binary Search

"""


#always have to skip over the mid

def order_agnostic_b_search(arr, key, start, end):

    while start <= end:
        mid = int(start + (end-start) /2)

        if key == arr[mid]:
            return mid
        
        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1 # not found

"""
same character, at least k distance apart
"""

def reorg( str, k):
    if k <= 1:
        return str
    
    char_map = {}
    for char in str:
        char_map[char] = char_map.get(char, 0) + 1
    
    max = []

    for char, freq in char_map.items():
        heappush(max, (-freq, char))

    queue = deque()
    res = []

    while max:
        freq, char = heappop(max)

        res.append(char)

        #decrement frequency
        #but because it is max heap, it is negative number, so "increment"
        queue.append((char, freq+1))    

        #queue must be length k, before releasing something from it
        if len(queue) == k:
            char, freq = queue.popleft()

            if -freq > 0:
                heappush(max, (freq, char))
    
    return "".join(res)