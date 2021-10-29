
"""
O(n^2)
Note: for small values of N
Note: best case sorted array = O(n) (does not enter while loop)

1. Work left to right of array
2. At each point, loop left, if find an item of larger value, switch places
3. Keep moving forward
"""

def insertionSort(arr):
	for i in range(1, len(arr)):
		moving = i-1
		key = arr[i]
		while (moving >= 0) and key < arr[moving]:
			arr[moving+1] = arr[moving]
			moving -= 1
		arr[moving+1] = key
	return arr

def main():
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    # arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = insertionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()