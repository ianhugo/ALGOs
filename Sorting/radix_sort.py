"""
Radix Sort
1. Have an input array
2. Have bins for each digit 0-9
3. Sort based on units, tens, hundred, thousands . . .
4. After each sort to bins, stitch them back together
5. Sort in that order again

Why it works:
with each successive sort, we get a sequence, sort in that sequence

Complexity:
theoretically O(n)

BUT because need to keep copying/stitching lists, 
complexity could be higher
large constant factors hidden, extra space

d = digits in input integers
b = base of represeting numbers
O(d * (n+b))

k = max number of digits
d = O(lg_b (k))

capping k at n^c, c - constant
we get
O(n lg_b (n))

If numbers are represented in base n, b = n
running time is O(n)

"""


def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    #use given exponent to find value for that digit
    for i in range(0, n):
        index = arr[i] // exp1 
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    #help aim where the output land
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
 
 
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
 
# Function Call
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i])