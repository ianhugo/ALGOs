
"""
Counting sort

if range of input data, not much bigger than number of objects

O(n) time
space proportional to range of data

this allows for negative numbers as well

1: calculate range in the array (will have min subtracted)
2: create an array for this range
3: iterate through, count occurences for each element of the array
(when adding, note that the min was subtracted)
4: now we have a count array full of cardinality
5: add the left hand, to current, to convert cardinality to position
6: loop backwards on output array
(when adding, note that the min was subtracted)

"""
# The function that sorts the given arr[]
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    #keep looping, as go through each element
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr