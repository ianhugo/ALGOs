"""
General Pattern

Given: 
- weight and profits of N items (two attributes)
- limit on capacity weight (restriction on one attribute)  
- 0/1, each item only once

Want: 
- maximize profit
- optimize on non-restricted attribute



"""

"""
Brute Force
"""

def knapsack_recur(profits, weights, capacity, curr_idx):
    """
    weights = constant array
    profits = constant array
    capacity = capacity left
    curr_idx = index in items to check

    Intuition:
    - go through all branches
    - at each level choose and not choose
    - fully compute when hit base case
    - choose maxima on recursive callback

    Time Complexity: 2^n exponential
    each item has two possible options
    which can vary with each
    """

    #if no more capacity left
    if capacity <= 0 or curr_idx >= len(profits):
        return 0

    #include this node
    profit1 = 0
    if weights[curr_idx] <= capacity:
        profit1 = profits[curr_idx] + knapsack_recur(\
        profits, weights, capacity - weights[curr_idx], curr_idx+1)

    #not include this node
    profit2 = knapsack_recur(profits, \
        weights, capacity, curr_idx + 1)
    
    return max(profit1, profit2)

"""
NOTE: there are overlapping subproblems
given capacity x left, should we choose item a
"""



"""
Top-Down Memoization

O(N * C) space and time
C = capacity

What is the DP table?
- what is changing?
- what capacity?
- given choice, what profit?
(NOTE: choice can be saved elsewhere)

IDEA:
- yes or no include this item
- if yes, decrement capacity, consider next item yes or no
- if no, keep capacity, consider next item yes or no
- thus consider all permutations
- with memoization cancel redundant computation

Visual:
- 2-d table
- each row = items
- each column = remaining capacity
- start at right low tip
- include item, jump across capacity on same row, then go up
- not include, go up one row, same capacity
- for both, now consider include or not include

- on recursive call-back
- included: profit of item + recursed max
- not included: recursed max
- take maxima

IDEA: 
- have the profit if include this item
    - recursed with less capacity
- have the profit if not include this item
    - recursed with more capacity

Observation:
- "delayed" computation
- post-processing


"""

def solve_kp(profits, weights, capacity):
    
    #2d matrix of -1 s
    dp = [[-1 for x in range(capacity+1)]for y in range(len(profits))]

    return knapsack_recur2(dp, profits, weights, capacity, 0)


def knapsack_recur2(dp, profits, weights, capacity, curr_idx):
    """
    NOTE: passing down table"""

    #if no more capacity left
    #or out of bounds
    if capacity <= 0 or curr_idx >= len(profits):
        return 0

    #check first
    #note table stores max profit given some choice
    #at this point
    #could adjust to save exactly what choice
    if dp[curr_idx][capacity] != -1:
        return dp[curr_idx[capacity]]

    #include this node
    profit1 = 0
    if weights[curr_idx] <= capacity:
        profit1 = profits[curr_idx] + knapsack_recur(\
        profits, weights, capacity - weights[curr_idx], curr_idx+1)

    #not include this node
    profit2 = knapsack_recur(profits, \
        weights, capacity, curr_idx + 1)
    
    dp[curr_idx[capacity]] = max(profit1, profit2)
    return dp[curr_idx][capacity]


"""
Bottom-up DP
O(N * C) space and time

- have dp table
- rows = items
- columns =  remaining capacity
- value = profit
- maximized profit(include or not include current)
- include: add profit, decrement capacity, find solution upstairs
    - check if possible
- exclude: keep capacity, find solution upstairs


Difference from Top-Down:
- fill out every cell
- pad edge cases
- sorted table?
- jumps to already calculated value,
    instead of to be calcualted value

Returning Result:
- check if took value from above
    - if not, then move down same item
    - if yes, continue
- continue this hopping until hit capacity 0

"""

def solve_knap(profits, weights, capacity):

    n = len(profits)

    #input value checks
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    #initialize
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    #populate for capacity 0
    #NOTE: a bottom-up thing
    #need to fill out edge cases, pad values
    for i in range(0, n):
        dp[i][0] = 0
    
    #fill out for item 1
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    #process all items
    for i in range(1, n):
        #process all capacities:
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0

            #include item
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
                #go up one item, decremented capacity
                #get max profit from that
            
            #go up one item, same capacity
            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)
    
    return dp[n-1][capacity]

"""
Space Complexity Optimize
- at each point, need two values from previous computation
    1: if include, dp[i-1][c-weight_i]
    2: if not include, dp[i-1][c]
- if compute 

O(C) space complexity
"""

"""
Intuition:
- when fill out next row, for item i
- go through each capacity
- at each capacity, decide
    - (if possible) include oneself, decrement capacity
        and refer to previous row
    - exclude oneself, keep capacity, refer to previous row

NOTE: always refering to previous
NOTE: previous refers to previous
NOTE: if want optimal solution, it is in last row anyway
NOTE: can have a separate keeping track of what 
        basket of goods for prev[i]

- use (i-1)%2 = previous
- use (i)%2 = current
- why? dynamically know which is curr/prev
- don't need to copy and paste stuff around
"""

def solve_knap2(profits, weights, capacity):
    
    n = len(profits)
    if capacity <= 0 or n ==0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity+1)] for y in range(2)]

    #if only one weight
    #take it if less than capacity (satisfies constraint)
    #padding values
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0] #setting value
    
    #loop through all items
    for i in range(1, n):
        #loop through all capacities
        for c in range(0, capacity+1):
            profit1, profit2 = 0, 0

            #include the item
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i-1)%2][c-weights[i]]
            
            #exclude the item
            profit2 = dp[(i-1)%2][c]

            dp[i%2][c] = max(profit1, profit2)
    
    return dp[(n-1)%2][capacity]

"""
ABSOLUTE Space Optimization
use one array

smaller O(C) space complexity

IDEA: 
- for each item, go from capacity -> 0 
- when computing for capacity k
    can refer to preceding cells, which are from previous
    at any point, refering to preceding, never backwards
- note: for each cell always referring to the previous row
        but at different positions

"""

def solve_knap3(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n ==0 or len(weights) != n:
        return 0
    
    dp = [0 for x in range(capacity+1)]

    #padding values
    #if only one weight, use that
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0

            #include
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            
            #exclude
            profit2 = dp[c] #previous at this cap

            dp[c] = max(profit1, profit2)