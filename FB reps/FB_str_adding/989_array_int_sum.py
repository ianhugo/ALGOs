"""
Given: array form of integer, num
Want: array form result of sum

IDEA:
- use k as carry
- add to lowest digit
- update carry
- go to higher digit

"""

def solve(arr, k):
    #normal bit
    for i in range(len(arr)-1, -1, -1):
        if not k:
            break
        k, arr[i] = divmod(arr[i]+k, 10)
    #carry bit
    while k:
        k, a = divmod(k, 10)    #k ,a = (k/10, k%10)
        arr = [a] + arr         #add element a and current a, for new a
    
    return arr