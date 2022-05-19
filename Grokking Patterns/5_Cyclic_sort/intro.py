"""
When: arr of numbers, in a given range (1 to n)
Want: sorted

How:

Example:
Given: unsorted arr[n] from 1 to n
has duplicates, some missing numbers
Want: missing numbers

Approach:
sort: place number at correct place
iterate: over all indices, find ones that don't match

flavors:
0: vanilla sort
1: there are duplicates
2: there are illegal values (smaller than or larger than range) = missing values
(illegal value will be placed where the missing one is usually)

Approaches:

----------------------------------------------
0. Cyclic Sort 0 (n range, n slots)
- while loop, with pointer i
- at i, arr[i] = j
- check if arr[i] == arr[j] (do they match) (match = in right place)
    - if not, switch, now value orginially at i (j), is at correct position j
    - now we have a new number at our position, do again
    - if yes, then we have placed the current one, can move to next 
O(n)


-----------------------
1. Cyclic Sort 1 (n+1 range, n slots) (missing/dup)
- cyclic sort, but move on if current is out of range
- (will go forwards and backwards)
- missing index will have the larger number
- iterate through after cyclic sort to find


-----------------------

2. Cyclic Sort 2: all missing/duplicate
- cyclic sort
- iterate through for discrepancy
- if one duplicate, can stop early (once find that arr[i] == arr[j]) (can also use slow-fast pointers = no modify)
- keep index too?


-----------------------

3. Modified Cyclic Sort (first missing positive)
- there is some range
- want first gap in the sequence (smallest missing positive number)
- prune, ignore out of range (too small, too large)
- "selective cyclic sort"
- careful boundary condition


-----------------------

4. Modified Cylic Sort v2 (k missing positives)
- check until out of range (add )
- when out of range, memoize all that we have left
- check each time
(issue, illegal values might be the "next" missing value, so need to check)


-----------------------

5. Check for duplicate, no edits
- cyclic sort + fast/slow pointers
- keep following through
- will arrive at same point twice if cycle
- but doesn't remember index, need to find length of cycle, then find start of cycle






YARD
- iterate through
- at i, have arr[i] value = j
- arr[i] should be at index j
- go to arr[arr[i]] (arr[j]), swap arr[i] and arr[j], go to arr[arr[j]]

"""