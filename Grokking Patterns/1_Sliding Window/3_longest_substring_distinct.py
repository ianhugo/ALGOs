"""
STATEMENT:
Given: string
Want: substring that is longest
    with distinct characters

STRATEGY:
- max_length, max_start
- wind_start, wind_end
- alphabet hash 
- increment until find duplicate character
- shrink until no more duplicate character
- update max_length, max_start (with wind_start)
- update char map[new_char] = position
- check, if char already taken
- take max between last position and cur wind_start = new wind_start
"""

def distinct_substring(str1):
    """
    TIME: O(N)
    SPACE: O(K) (k = number of chars)
    SPACE: O(1) if fixed array
    """
    wind_start = 0
    max_len = 0
    char_index = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_index:
            wind_start = max(wind_start, char_index[right_char])
        
        char_index[right_char] = window_end

        max_lent = max(max_len, window_end - wind_start +1)
    
    return max_lent



"""
This problem follows the Sliding Window pattern, 
and we can use a similar dynamic sliding window strategy 
as discussed in Longest Substring with K Distinct Characters. 
We can use a HashMap to remember the last index of each character 
we have processed. Whenever we get a duplicate character, 
we will shrink our sliding window to ensure that we always have 
distinct characters in the sliding window."""