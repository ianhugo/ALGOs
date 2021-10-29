"""
O(n^2)

NOTE: 
best case = worst case = O(n^2)
have to iterate whole subarray to ensure it is minimum

“opposite of Insertion Sort”
1. Work left to right of array
2. At each index_k, loop right
	1. pointer1 = minimum current (min_idx)
	2. pointer2 = iterate through (j)
	3. set both as index_k to start
	4. iterate through, find the minimum
3. switch pointer1 and index_k
4. increment index_k
"""

def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr

def main():
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    # arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = selectionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()