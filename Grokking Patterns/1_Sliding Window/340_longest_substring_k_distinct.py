"""
STATEMENT:
Given: string, int k
Want: longest substring
with at most K distinct characters


Strategy:
- Track max_length, current distinct
- sliding window pop off
- alphabet array, keep track of earliest
    (hash map could be even smaller space)
- shrink to that
"""

def longest_substring_with_k_distinct(str1, k):
    """
    Time; O(n)
    Space: O(k)
    """
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
    if right_char not in char_frequency:
        char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
        left_char = str1[window_start]
        char_frequency[left_char] -= 1
        if char_frequency[left_char] == 0:
            del char_frequency[left_char]
        window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
    return max_length