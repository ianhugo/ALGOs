"""
theta(n lg n)
O(n) for additional L, R arrays at each level

NOTE:
slower to other sort algos for smaller tasks
sorts even if sorted
better for linked lists

1. Partition array into halves
2. Recursively partition, until single arrays
3. Merge into sorted larger arrays
4. pointer at each of 2 smaller subarrays
5. compare values at pointers
6. put smaller value at subarray_A into larger array
7. increment pointer of subarray_A
8. one side finishes faster, finish up remaining
9. repeat until fully done with layer, then repeat
"""

def partition(arr):
	if len(arr)> 1: #recursion condition
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		L = partition(L)	#recursion
		R = partition(R)	
		sorted = mergeSort(L, R, arr)
	else:	#arr of len 1
		sorted = arr
	return sorted

def mergeSort(L, R, arr):
	i = j = k = 0
	
	while (i < len(L)) and (j < len(R)):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	
	while i< len(L):	#cleanup
		arr[k] = L[i]
		i += 1
		k += 1
	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1

	return arr


def main():
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    # arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = partition(arr)
    print(arr)

if __name__ == "__main__":
    main()