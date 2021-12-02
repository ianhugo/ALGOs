"""
STATEMENT:
Given: str1, pattern
Want: 
- Bool
- if str1 contains substring of any permutation of pattern

Permutation: re-arranging of characters of string

STRATEGY:
- sliding window
- process pattern -> hash map[char] = [target, curr, last_pos]
- wind_start, exist_bool, all_chars_bool
- iterate wind_end
- if wind_end is a key, check if already have target number
    - if not, continue
    - if so, shrink, and decrement stuff, until last_pos
- stop when?

LEARNED:
hacky type things
might be solved by balancing restrictions
need to check less things
"""


def find_permute(str1, pattern):
    """
    Time: O(n+m)
    Space: O(m)
    m = length of pattern
    """
    wind_start, matched = 0, 0
    char_freq = {}

    #prep
    for chr in pattern:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] +=1
    
    for wind_end in range(len(str1)):
        right_char = str1[wind_end]
        if right_char in char_freq:
            char_freq[right_char] -=1 #decrement
            if char_freq[right_char] ==0: #decrement logic
                matched +=1

        #stopping condition
        if matched == len(char_freq):
            return True

        #if non matched characters, window keeps expanding
        #but will hit limit
        #the condition to true above, is when everything is matched
        #within the confines of the length restrict
        if (wind_end - wind_start+1) >= (len(pattern) -1):
            left_char = str1[wind_start]
            wind_start +=1
            if left_char in char_freq:
                #if was fully matched, need to adjust
                if char_freq[left_char] == 0:
                    matched -=1
                #increment means need to find more
                char_freq[left_char] +=1 #put char back
    
    return False
