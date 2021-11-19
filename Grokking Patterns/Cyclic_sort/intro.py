"""
When: arr of numbers, in a given range

Example:
Given: unsorted arr[n] from 1 to n
has duplicates, some missing numbers
Want: missing numbers

Approach:
sort: place number at correct place
iterate: over all indices, find ones that don't match

Approaches:

1. Cyclic Sort 1
- iterate through
- at i, have arr[i] value = j
- arr[i] should be at index j
- go to arr[arr[i]], swap arr[i] and arr[j], go to arr[arr[j]]

2. Cyclic Sort 2: missing/duplicate
- cyclic sort
- iterate through for discrepancy
- if one duplicate, can stop early
- keep index too?

3. Modified Cyclic Sort
- there is some range
- want first gap in the sequence (smallest missing positive number)
- prune, ignore out of range (too small, too large)
- "selective cyclic sort"
- careful boundary condition

4. Modified Cylic Sort v2 (continued)
- check until out of range
- when out of range, memoize all that we have left
- check each time

5. Check for duplicate, no edits
- keep following through
- will arrive at same point twice if cycle
"""