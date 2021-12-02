"""
Given: weight array, profit array, constraint C
(can choose infinite times)
Want: subset of maximized profit

"""


"""
BRUTE:
- try all combinations

for each item:
    for item1 range()
        for each item2"
            for item 2 range()
"""

def solve(profits, weights, capacity):
    return solve_recur(profits, weights, capacity, 0)

def solve_recur(profits, weights, capacity, curr_idx):

    n = len(profits)

    #validations
    #edge cases
    if capacity <= 0 or n == 0 or len(weights) != n or curr_idx >= n:
        return 0
    
    profit1 = 0

    #new set with 1 of current item
    #this will lead to multiple of one item
    if weights[curr_idx] <= capacity:
        profit1 = profits[curr_idx] + solve_recur(profits, weights/
            capacity - weights[curr_idx], curr_idx)
    
    #skip item, do next item
    profit2 = solve_recur(profits, weights, capacity, curr_idx+1)

    #maximize
    return max(profit1, profit2)

"""
Top-Down with Memoization

- pre check
- fill out table, at each, the maximized profit
- for this capacity, what is the maximized profit
- cache result
"""

def solve1(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    return solve1_recur(dp, profits, weights, capacity, 0)

def solve1_recur(dp, profits, weights, capacity, curr_idx):
    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) != n or curr_idx >= n:
        return 0
    
    if dp[curr_idx][capacity] == -1:

        profit1 = 0
        if weights[curr_idx] <= capacity:
            profit1 = profits[curr_idx] + solve_recur(profits, weights/
            capacity - weights[curr_idx], curr_idx)
    
    #skip item, do next item
    profit2 = solve_recur(profits, weights, capacity, curr_idx+1)

    #maximize
    dp[curr_idx][capacity] = max(profit1, profit2)

    return dp[curr_idx][capacity]

"""
Bottom-up:
"""

def solve3(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n or curr_idx >= n:
        return 0
    
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    for i in range(n):
        dp[i][0] = 0
    
    for i in range(n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i][c-weights[i]]
            
            if i>0:
                profit2 = dp[i-1][c]
            dp[i][c] = profit1 if profit1>profit2 else profit2
    
    return dp[n-1][capacity]
