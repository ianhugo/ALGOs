"""
Given: array of integers, target sum S
Want:
- assign + or - to each integer (all of them needs one)
- subsets that lead to target sum S

IDEA:
Sum1 - Sum2 = target
Sum1 + Sum2 = total

Total - target = Sum1 + Sum2 - Sum1 + Sum2
Total - target = 2 * Sum2
"""