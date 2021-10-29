from insertion_sort import insertionSort

"""for data across a certain range
uniformly distributed for O(n)

depending on number of elements and max value, create number of buckets

depending on computation, put a certain range into buckets
insertion sort each bucket
then stitch together
"""

def bucketSort(arr):
    """
    slot_num = choose number of slots
    """
    buckets = []
    max_val = max(arr)
    min_val = min(arr)
    arr_f = []

    if arr == None or len(arr) == 0 or min_val == max_val:
        return
    
    n = len(arr)
    m = max_val - min_val +1
    num = int(m/n +1)

    buckets = []

    for i in range(num):
        buckets.append([])
    
    for j in range(n):
        index = int((arr[j]-min_val)/m)
        buckets[index].append(arr[j])
    
    for bucket in buckets:
        if bucket != []:
            arr = insertionSort(bucket)
        arr_f += arr
    
    return arr_f




def main():
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    # arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = bucketSort(arr)
    print(arr)

if __name__ == "__main__":
    main()