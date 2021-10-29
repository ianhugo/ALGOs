"""
Worst = O(n^2)
Best = O(n), sorted

1. Compare consecutive items
2. Swap if L > R
3. Last Item will now be largest (“bubbled” to the top)
4. Repeat for array, except for last item
5. conditional, for early break
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        noSwap = True
        for j in range(0, (n-i-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                noSwap = False
        if noSwap:
            break
    return arr
    
def main():
    arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,-1]
    # arr = [2, 6, 5, 2, 6, 8, 6, 1, 2, 6]
    arr = bubbleSort(arr)
    print(arr)

if __name__ == "__main__":
    main()