import random

def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 
# Partition routine using the Dutch national flag algorithm
# three pointers: start, mid, end
# end goal: start, end = denote the mid range
# end state: mid pointer has passed end
def partition(A, start, end):
 
    mid = start
    pivot = A[end]
 
    while mid <= end:
 
        if A[mid] < pivot:
            swap(A, start, mid)
            start += 1
            mid += 1
 
        elif A[mid] > pivot:
            swap(A, mid, end)
            end -= 1
 
        else:
            mid += 1
 
    # `A[start … mid-1]` contains all occurrences of a pivot
    return start - 1, mid, pivot
 
 
# 3–way Quicksort routine
def quicksort(A, start, end):
 
    # base condition for 0 or 1 elements
    if start >= end:
        return
 
    # handle 2 elements separately as the Dutch national flag
    # algorithm will work for 3 or more elements
    if start - end == 1:
        if A[start] < A[end]:
            swap(A, start, end)
        return
 
    # rearrange elements across pivot using the Dutch
    # national flag problem algorithm
    t = random.randint(start, end)
    A[t], A[end] = A[end], A[t]

    x, y, pivot = partition(A, start, end)
    print(A, pivot)
    # recur on sublist containing elements that are less than the pivot
    quicksort(A, start, x)
 
    # recur on sublist containing elements that are more than the pivot
    quicksort(A, y, end)
 
 
if __name__ == '__main__':
 
    # a = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    a = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
 
    quicksort(a, 0, len(a) - 1)
 
    # print the sorted list
    print(a)
 