"""
Given: string s
Want: different perms of lowercase/uppercase

Strategy:
loop through once note all char positions

each step: lower case or upper case
pass in next element
hit base case when queue is empty
"""

def case_permute(str1):
    perms = []
    perms.append(str1)

    for i in range(len(str1)):
        if str1[i].isalpha():   #alphabet
            n = len(perms)
            #for each character
            #take each permutation existing
            #counted by n
            #copy once, change case
            #append again
            for j in range(n):
                tmp = list(perms[j])

                tmp[i] = tmp[i].swapcase()
                perms.append(''.join(tmp))  #back into list