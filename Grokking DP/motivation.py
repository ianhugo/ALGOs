"""
https://www.youtube.com/watch?v=iv_yHjmkv4I

Overlapping Subproblems:
- smaller broken down problems
- depend on solving overlapping smaller problems

Optimal Substructure:
- to solve the biggest problem optimally
- construct from optimal solution to smaller problems

Want to calculate all combinations
Want to remember what has been solved
Make Recursion more efficient

the DP difference
- check before computing
- store value before return
- be careful of out of bounds referencing
- or define it beforehand

Top-down Memoization:
- recursively solve smalelr sub-problems
- cache result

Bottom-up Tabulation:
- not recursion
- typically, fill out n-dimensional table

1. Start with Brute Force
2. Optimize with Memoization/Tabulation techniques


Observation 1:
- start with brute force
- optimize with memoization/tabulation
- check if result
- store after result

Observation 2:
- what to store in the dp table?
- wider scoping parameters
- ask: what variables are changing
- the smallest choice: include not to include
- can be baked into the solution


"""