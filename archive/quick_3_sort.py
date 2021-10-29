"""
at partition
do another sweep from the right
"""

def partition(arr, low, high):
    print("original ", arr)
    i = low -1
    z = high
    arr= find_pivot(arr, low, high)
    pivot = arr[high]
    for j in range(low, high-1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # arr[i+1], arr[high] = arr[high], arr[i+1]
    print("first half", arr, i)
    for k in range(high-1, low, -1):
        if arr[k] > pivot:
            z -= 1
            arr[z], arr[k] = arr[k], arr[z]
    print("second half", arr, z)
    arr[z], arr[high] = arr[high], arr[z]
    
    print("pivot used ", pivot)
    print("final", arr)
    return arr, i+1, z+1

def quick_3_sort(arr, low, high):
    print("low", low)
    print("high", high)
    if (high - low) < 2:
        return arr
    if low< high:
        arr, pi1, pi2 = partition(arr, low, high)
        arr = quick_3_sort(arr, low, pi1)
        print("switch")
        arr = quick_3_sort(arr, pi2, high)
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
    arr = [0, 1, 2, 0, 2, 1, 1]
    arr = quick_3_sort(arr, 0, (len(arr)-1))
    print(arr)

if __name__ == "__main__":
    main()
    