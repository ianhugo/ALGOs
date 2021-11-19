"""
When: given a tree, need to find which nodes to include
to satisfy some constraint

use Recursion with DFS


Approaches:

1. Root to Leaf searches:
- do DFS, with recursion, backtracking

2. Finding Specific Sequence
- pre-processing: 
    - check if leaf
    - check if exceed length
    - check if supposed next index-value of target index
    - check if stopping success condition
- pass down:
    - check left, check right
    - target sequence
    - next index to check

3. Finding all paths that fulfill requirement
- pre-processing:
    - check if leaf
    - from received current path list, add curr_node, check if meet conditions
    - if so, append to results
- pass down:
    - check left
    - then check right
    - target spec
    - current paths
- post-processing:
    - use backtrack
    - remove current level node
    - as need check left, then check right
    - need to change curr_path

4. Need to check subtree quality for global, but subtree has one path useful not both
- compute end value of curr level
- recurse on left, recurse on right, together with now node compute
- return the maximal/minimal subtree side, including own
(imagine, trying to find some tree with some quality
each node, can be the root with the desired tree)
"""