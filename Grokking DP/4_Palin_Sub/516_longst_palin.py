"""
Given: string
Want: longest palindromic subsequence

Can: delete some elements
Cannot: change order

BRUTE FORCE:
dumbest: make all possible substrings
next: choose every character as start, expand to see the longest

Intuition:
- make calls on each start, end pair
- base = length 1 palindrom
- each position 3 choices
- same (then shrink both sides), add 2 to length, RETURN
- if not    = shrink from start
            = shrink from end
- on return, take the max

IDEA:
- if unmatched, max of two unbalacned shorter ones
- if matched, 2 + value of [start+1][end-1]

"""
import math

def lps(st):
    return recur(st, 0, len(st)-1)

def recur(st, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if st[start] == st[end]:
        return 2 + recur(st, start+1, end-1)
    
    c1 = recur(st, start+1, end)
    c2 = recur(st, start, end-1)
    aa = max(c1, c2)
    
    return math.max(c1, c2)

"""
Top-Down
changing: start, end index
store in 2d array
or hash of key start, end

TIME: no more than O(n^2)
aka filling the table

"""

def lps2(st):
    n = len(st)
    dp = [[-1 for _ in range(n)]for _ in range(n)]

    return recur2(dp, st, 0, n-1)

def recur2(dp, st, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if dp[start][end] == -1:

        if st[start] == st[end]:
            dp[start][end] = 2 + recur2(dp, st, start+1, end-1)
        else:
            c1 = recur2(dp, st, start+1, end)
            c2 = recur2(dp, st, start, end-1)
            dp[start][end] = max(c1, c2)
    
    return dp[start][end]


"""Bottom-up

QUESTION: what is the order of filling out the table
- from bottom to up

in terms of dp table
- diagonal filled, as these are 1 length palindromes
- from the 1 position to the right
- at each point, if unmatched
- then take the max of (left, down)
(these two are 
down: dp[start+1][end] 
left: dp[start][end-1])
- if matched, take diagonal left down
diagonal left down: dp[start-1][end-1]

WHY only above diagonal filled:
start index must be same, or smaller than end

PICTURE:
- sort of filled backwards
- low level to top level
- at each level left to right
- start index, start from back
- then expand to the end

O(n^2)
"""

def lps3(st):
    n = len(st)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):  #go through all
        dp[i][i] = 1    #all one elemnt = 1

        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                if st[start] == st[end]: #ok
                    dp[start][end] = 2 + dp[start+1][end-1]
                else:   #ok
                    dp[start][end] = max(\
                        dp[start+1][end], dp[start][end-1])
    
    return dp[0][n-1]

