
"""


1. Basic
TOP-DOWN: 
- base: empty string on one, return 0
- if match      -> chop both
                -> 1 + recur(str1, str2)
- if unmatch    -> chop str1, recur(str1-, str2)
                -> chop str2, recur(str1, str2-)
                -> return max of both

BOTTOM-UP:
- base: empty string on one, return 0
- go row by row, column by column
- row = str1, column = str2
- pad with empty string
- start with str1 first character
- if match      -> chop both
                -> 1+ dp[i-1][j-1] (diagonal up left)
- if unmatch    -> chop str1, check dp[i-1][j]
                -> chop str2, check dp[i][j-1]
                -> max(these two cells)

NOTE: sort of like include, exclude

-----------------
2. Longest Increasing Sub (LIS)

TOP-DOWN
- checking, storing cache
- passing: curr idx, prev, idx
- check for if increasing
- include or exclude

BOTTOM-UP
- 1d res, all are LIS of 1
- iterate through each index
- for each index i
    compare with all previous
    if smaller than a previous j
    take dp[j] +1
    take max with dp[i]




"""