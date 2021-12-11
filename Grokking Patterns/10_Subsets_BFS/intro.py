"""
When: 
- want Permutations, Combinations of given set
- need to make subsets
- use some form of Recursion

Idea:
- imagine it as a BFS structure
- explore all options at this layer
- then explore next layer
- at each step do some form of selection
- at each step do some form of operation

Approaches:

----------------------------------------------
1. All Subsets (78)
- copy all, do action
- append to previous (what was copied)


-----------------------
2. All Subsets with Duplicates (78 with duplicates)
- copy all, do action
- if duplicate, copy what was acted on last, do action on that, append


-----------------------
3. Permutation Placement (46, 22) 
- at each layer, do action
- at each layer, action on all possible positions


-----------------------

4. Branching 0.5 (784)
- each layer a position
- each layer two choices


-----------------------

4.1. Branching 1 (320 abbrev)
- iterate from left to right
- at each layer, at each position, two branches
- do action, not do action


-----------------------

5. Branching 2 (241 compute expression, unique BST)
- iterate from left to right
- at each layer, at each position
- slice into two
- break into subgroup, call function again (recursion)
- do at each position, slice into two again


----------------------------------------------


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