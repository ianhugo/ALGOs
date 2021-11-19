"""
When: 
- want Permutations, Combinations of given set
- need to make subsets
- use some form of Recursion

Idea:
- imagine it as a BFS structure
- at each step do some form of selection
- at each step do some form of operation

Approaches:
1. Basic
- copy all, do action
- append to previous (what was copied)

2. Basic 2
- copy all, do action
- if duplicate, copy what was acted on last, do action on that, append

3. Permutation Placement
- at each layer, do action
- at each layer, action on all possible positions

4. Branching 1
- iterate from left to right
- at each layer, at each position, two branches
- do action, not do action


5. Branching 2
- iterate from left to right
- at each layer, at each position
- slice into half
- break into subgroup, call function again (recursion)
- do at each position, slice into half again


Observation 20 Subset pattern:
- take note of what choice needs to be made at each level
- permutation = place at each position . . .
- do some examples

Observation 21 Subset pattern:
- there are two patterns
- 1: make a copy of everything, apply changes to a copy of it
    - number of items have doubled
- 2: apply changes to all of them, where possible

Observation 22 Subset pattern:
- apply changes based on condition
- apply different types of changes
- apply each change to all last states
"""