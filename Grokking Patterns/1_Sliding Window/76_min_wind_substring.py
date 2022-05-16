"""
STATEMENT:
Given: string, pattern
Want: minimum window substring
- including all characters

STRATEGY:
- sliding window
- min_length
- hash map similar logic to str_permute
- shrink until: hit all again

OPTIMIZATION:
iteration depends on the string being window slide over
O(n + m)
do another pre: where filter the string for only characters there
keep track of the non-filtered positions
"""

def find_substring(str1, pattern):
    """
    O(n+m) time
    O(m) space for hashmap
    O(n) space for resulting substring"""
    wind_start, matched, sub_start = 0, 0, 0
    min_length = len(str1) +1
    char_freq = {}

    #prep
    for chr in pattern:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] +=1
    
    for wind_end in range(len(str1)):
        right_char = str1[wind_end]
        if right_char in char_freq: #matched
            char_freq[right_char] -=1

            if char_freq[right_char] >= 0:  #count every matched
                matched +=1
        
        #shrinking
        #stop when remove matched character
        #keep shrinking while still desirable
        while matched == len(pattern):

            #matched and have smaller
            if min_length > (wind_end - wind_start +1):
                min_length = wind_end - wind_start +1
                sub_start = wind_start
            
            #shrink it
            left_char = str1[wind_start]
            wind_start +=1
            #all chars must be 0 or -ve at first
            #if at zero, then matched change
            #that means breaks outer condition
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -=1
                char_freq[left_char] += 1
    
    if min_length > len(str1):
        return ""
    
    return str1[sub_start: sub_start + min_length]