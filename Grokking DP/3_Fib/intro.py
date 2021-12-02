"""
Given: array of things, or target value
Need: jump around, in constrained ways
Want: value related to number of jumps

Intuition: array jumping

Form:
- solution[n] depends on solution[n-1], solution[n-2] . . .

NOTE: dp tables might have to do 1 extra unit of length 
        used as padding, to "kickstart"

NOTE: base cases, are 0, 1, 2
(finish, 1 off odd, 2 off even)


Pattern 1: Fib
- jumping between values
- avoid recomputation

Pattern 2: Ways to jump to end
- top-down: start from back, try all possible jumps
- bottom-up: each position, sum up number of possible jumps from before

Pattern 1: array jumps with fixed choices
- O(n)
- sum ways
- take max or min
- other operations . . .

Pattern 2: array jumps with variable choices at index
- O(n^2)
- at each step, try all possible, which could at worst be O(n)


----------------------------------------------

Pattern 1:
- array of numbers, or jumping numbers
- dp[i] depends on fixed number of previous entries
- fib: sum it
- staircase, number factors: count number of ways to reach
- staircase with fee: minimum of previous
- O(n)
-----------------------

Pattern 2:
- array of numbers
- dp[i] depends on variable number of future entries
- top-down:     go DFS
                for each dp[i] loop through options
                on recurse, take min/max of options
        
- bottom-up:    go BFS
                for each dp[i] loop through options
                update partial values of options (min/max)
- O(n^2)

-----------------------

Pattern 3:
- array of numbers
- two types of skips
- want maximal value
- at each point, include or exclude
- include = value[i] + prev1
- exclude = prev2
-O(n)
(similar to other fib, but choose one and include oneself in other)
(odd: how it is filled out
dp[i] looks backwards
because of choice in this node, imply choices in previous node)


NOTE: with padded value of start, start there
NOTE: reduce to the lowest lowest, first decision
NOTE: max value at this location (robbed, or skipped?)
"""