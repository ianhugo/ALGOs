"""
at partition
do another sweep from the right
"""

def partition(arr, low, high):
	i = (low - 1)	#boundary for lower subarray
	z = high
	arr, pivot = find_pivot(arr, low, high)
	for j in range(low, high-1):
		if arr[j] <= pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	for k in range(high-1, low, -1):
		if arr[k] > pivot:
			z = z - 1
			arr[z], arr[k] = arr[k], arr[z]
	arr[i+1], arr[high] = arr[high], arr[i+1]
    print("pivot used", pivot)
    
	return arr, i, z

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		arr, pi1, pi2 = partition(arr, low, high)
		arr = quickSort(arr, low, pi1-1)
		arr = quickSort(arr, pi2+1, high)
	return arr

def find_pivot(arr, low, high):
    if (high - low) < 2:
        pivot = low
    else:
        mid = len(arr)//2
        pivot = get_median(arr, low, mid, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    return arr, arr[high]  #return put pivot in last position

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
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    arr = quickSort(arr, 0, (len(arr)-1))
    print(arr)

if __name__ == "__main__":
    main()