"""
Given: two strings, have # character for backspace
Want: after backspace, strings equals?
O(n) time, O(1) space

Strategy:
- two pointers
- go from back, start comparing
- if get backspace, do skips
- break early if not matching
"""

"""
O(m+n)
m, n = lengths of strings

O(1) space"""

def backspace_cmp(str1, str2):
    idx1 = len(str1)-1
    idx2 = len(str2)-1

    while (idx1 >= 0 or idx2 >=0):
        i1 = nxt_valid(str1, idx1)
        i2 = nxt_valid(str2, idx2)
        if i1 < 0 and i2 < 0:  # reached the end of both the strings
            return True
        if i1 < 0 or i2 < 0:  # reached the end of one of the strings
            return False
        if str1[i1] != str2[i2]:  # check if the characters are equal
            return False
        
        #going backwards
        idx1 = i1 - 1
        idx2 = i2 - 1
    
    return True

def nxt_valid(str, idx):
    backspace_count = 0
    while (idx >= 0):
        #while loop catches two conditions
        #if not, then break
        #ensures go back twice on backspaces
        if str[idx] == '#':  # found a backspace character
            backspace_count += 1
        elif backspace_count > 0:  # a non-backspace character
            backspace_count -= 1
        else:
            break

        idx -= 1  # skip a backspace or a valid character

    return idx