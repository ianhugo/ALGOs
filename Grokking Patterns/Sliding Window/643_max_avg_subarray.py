
"""
STATEMENT:
Given: array, size K
Want: subarray with max average


Brute force: O(n^2)
Smart: O(n^2)

"""


def find_avgs_subarrays(K, arr):
    """
    find averages of all windows
    """
    result = []
    windowSum, windowStart = 0.0, 0

    #loop through array
    for windowEnd in range(len(arr)):
        
        #add next element
        windowSum += arr[windowEnd]
        
        #skip pass initial elements
        if windowEnd >= K -1:
            result.append(windowSum/K)  #chef up
            
            #subtract element
            windowSum -= arr[windowStart]

            #slide the window
            windowStart += 1
    
    return result


def max_sum_sub_array(k, arr):

    """
    calc averages, save max dynamically
    O(n) time
    O(1) space
    """
    max_sum, window_sum = 0.0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k -1:
            max_sum = max(max_sum, window_sum)
            window_sum == arr[window_start]
            window_start += 1
    
    return max_sum