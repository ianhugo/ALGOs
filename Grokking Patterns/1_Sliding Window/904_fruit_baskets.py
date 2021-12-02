"""
STATEMENT:
Given: single row of fruit tree array (arr of ints)
Want: maximize number of fruits in 2 baskets
- one type of fruit per basket
- starting from tree[x], pick one fruit from every tree
- stop when reach a tree, have 3 types now
- return max number of fruits picked

ANALOGY: Longest Substring with k distinct
STRATEGY:
- represent trees as row of ints
- sliding window
- result: [length, starting, #fruits]
- iterate until more than 3 types
- shrink until 2 types again
- then add again
- check each time, whether max(cur_len, max_len) changed
- if so, update starting position, max_length, #fruits in result arr

"""