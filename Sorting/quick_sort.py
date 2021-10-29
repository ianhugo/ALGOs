
"""
Worst case: O(n^2), bad pivot
Best case: O(n lg n)

NOTE: cache efficient, constant operations of quicksort

1. Choose Pivot, move to end of array
2. Pointer_Left, Pointer_Right
3. find itemL, first item from left >pivot
4. find itemR, first item from right <pivot
5. swap
6. stop when  Pointer_Right < Pointer_Left, or same
7. swap pivot with Poitner_Left
8. pivot now in correct position
9. recurse

Choosing pivot: (Median of Three)
1. Extract 1st, Mid, Last of array
2. Sort them
3. Use as pivot

in this implementation: only sweep from left is ok
"""
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return arr, i+1

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        arr= find_pivot(arr, low, high)
        arr, split = partition(arr, low, high) #sorted this sub range
        arr = quickSort(arr, low, split-1) #sort left side
        arr = quickSort(arr, split+1, high) #sort right side
    return arr

def find_pivot(arr, low, high):
    if (high - low) < 2:
        pivot = low
    else:
        mid = len(arr)//2
        pivot = get_median(arr, low, mid, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    return arr  #return put pivot in last position

def get_median(arr, low, mid, high):
	x = arr[low] - arr[mid]
	y = arr[mid] - arr[high]
	z = arr[low] - arr[high]
	if (x*y > 0):
		return mid
	if (x*z > 0):
		return high
	return low

def main():
    # arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = quickSort(arr, 0, (len(arr)-1))
    print(arr)

if __name__ == "__main__":
    main()