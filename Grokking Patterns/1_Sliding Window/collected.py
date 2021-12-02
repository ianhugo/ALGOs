"""

PATTERN 1: Simple

GIVEN: array, k
WANT: maximum sum, in subarray size k
STRATEGY:
- sliding window
- add to right, pop the left
- running max
>>>>>



-----------------------------------------
PATTERN 2: Shrinking

209
GIVEN: array, sum S
WANT: smallest subarray, with that sum
STRATEGY:
- sliding window w shrinking
- have a curr_sum
- when curr_sum reach/over target, try to shrink
- running min size, result store
>>>>>

340
GIVEN: array, k
WANT: subarray with max k distinct chars
STRATEGY:
- sliding window w shrinking
- track target with hashmap of chars
- when reach k distinct, try to shrink
- running max size, result store
>>>>>

904
GIVEN: array, k
WANT: subarray with max k fruits
STRATEGY:
- as above
>>>>>

424
GIVEN: string, k
WANT:   longest substring same letters
        replace k chars max
STRATEGY:
- sliding window w shrinking
- hash map tracking freq of each char
- have curr_max_letters (max updated when encounter new)
- use (wind_end - wind_start - curr_max) = what's to replace
- check this with k, if need to shrink
- use this to shrink, update hash
>>>>>

--------------------------
PATTERN 3: Pattern in array

567
GIVEN: string, pattern
WANT: bool, does string contain perm of pattern
STRATEGY:
- iterate pattern, store in hash
- store length of pattern = n
- tracking variable matched
- iterate through string, decrement freq, increment matched
- 1:    stop when, success, matched = n
- 2:    stop when (wind_end-wind_start) exceed pattern
        shrink, decrement hash, matched
>>>>>

438
GIVEN: string, pattern
WANT: anagrams of pattern in string
STRATEGY:
- same as 567
- store the found things
>>>>>

76
GIVEN: string, pattern
WANT: min window, containing characters
STRATEGY:
- same as 567
- running min length
- stop shrinking when removed a matched/needed char
- don't stop shrinking when just hit duplicate
>>>>>

30:
GIVEN: string, list of words
WANT:
- indices of substrings
- substring = concat of all given words, no overlapping
- words are same length
STRATEGY:
- similar to 567
- hash of words_seen
- iteration anchor at each word
- try to expand/fill
- stop when exceed counts
- process next word


"""