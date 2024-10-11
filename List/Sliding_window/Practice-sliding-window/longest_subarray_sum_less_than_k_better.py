def longest_subarray_sum_less_than_k(arr, k):
    n = len(arr)
    i, j = 0, 0
    sum_tot = 0
    max_size = 0
    res = []

    for j in range(n):
        # Add the current element to the total sum
        sum_tot += arr[j]
        
        # Shrink the window if the sum exceeds or equals k
        if sum_tot >= k:   # For optimal Approach change the 
            sum_tot -= arr[i]            # while to if only for neccesary conditions
            i += 1

        # Update the result if the current window is the longest
        if sum_tot < k :
            if j - i + 1 > max_size:
                max_size = j - i + 1
                res = arr[i:j+1]


    return max_size, res

# Example usage
arr = [1, 2, 3, 1, -1, 3, 5, 2]
max_len, res = longest_subarray_sum_less_than_k(arr, 10)
print('Size of the array is:', max_len)
print('The Subarray is:', res)
