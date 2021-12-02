"""
Given:
- attributes of items
- constraint on attribute
- maximize (optimize for a certain thing)
- can choose unlimited number of an item

Before with 0/1 Knapsack:
- two cases
- include item
- exclude item
- on recurse, operation

Now with Unbounded Knapsack:
- two cases
- include 1 more of this item
- skip to next item
- on recurse, operation

Bottom-up DP table:
- take above
- or take here + before

-----------------------
Pattern 1:
- simple unbounded ks
- incrementing, number of possible solutions

-----------------------
Pattern 2:
- max or min the count of valid combos


"""