"""
STATEMENT:
Given: string lowercase, int k
Want:
- allow replace k characters
- longest substring with same letters

STRATEGY:
- max_length, last_non_uniform, char_map[char] = [#, last pos]
- curr_max, next_max 
- start with first element
- iterate until hit k replaces
- shrink
    - if shrink and drop replacement, increment again
    - if drop below next_max, 
"""

def length_longest_substring(str1, k):
    """
    Time: O(n)
    
    Space: O(26)
    """
    wind_start, max_lent, max_repeat = 0, 0, 0

    freq_map = {}

    for wind_end in range(len(str1)):
        right_char = str1[wind_end]
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] += 1

        max_repeat = max(max_repeat, freq_map[right_char])  #best candidate to repeat
        #new max, will be because of new char
    
        #shrink when repeating characters original more than k
        #note: abstracted from tracking which letter is repeated
        if (wind_end - wind_start +1 - max_repeat) > k: #how many letter to replace
            left_char = str1[wind_start]
            freq_map[left_char] -=1
            wind_start += 1

        max_lent = max(max_lent, wind_end - wind_start +1)

    return max_lent