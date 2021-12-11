"""
GIVEN: num
- swap two digits at most once
WANT: max number

DRAFT: highest value in front

IDEA: each digit, larger digit that occurs later 
want to swap with largest digit that occurs latest

IDEA better:
- iterate from back
- track
    max_idx
    first_idx
    second_idx
- find the max
- check if this number can be swapped with max

"""
def maximumSwap(self, num):
    num = [str(d) for d in str(num)]
    max_ind, first_ind, second_ind = len(num)-1, 0, 0
    for i in range(len(num)-1,-1,-1):
        if(num[i]>num[max_ind]):    
            max_ind = i
            
        if(num[i]<num[max_ind]):    #if num[i] can be replaced with max_num on the right
            first_ind = i      
            second_ind = max_ind   
            
    num[first_ind],num[second_ind] = num[second_ind], num[first_ind]
    
    return("".join(num))