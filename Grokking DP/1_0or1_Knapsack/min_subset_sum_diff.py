"""
Given: set of positive numbers
Want: partition into subsets
minimum difference between subset sums

IDEA:
- row = include number i into the subset?
- column = want this target difference

min difference = if equal sum of two subset
so previous question, same dp table works
but?

so where is the answer?
either at the last row, last column
or any non-False position before that
"""