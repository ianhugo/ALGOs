"""
Given: expression with math symbols
Want: different parentheses placement to get results

Strategy:
add open parentheses
different palces to put end parentheses
open: after symbol
close: after int

1 + 2 * 3 -6 +7 * 8

1 -   1 + 2 - 

1 2 


Divide and Conquer
IDEA: when encounter symbol, split into left and right part

with Memoization


Approach:
- at each operator, add (, add ), no add
- adding after
- copy all each time
- conditions on (: can't be last operator
- conditions on ): need equal number of (
                    need to be 3+ indices after
- at end, finish up all parentheses
"""