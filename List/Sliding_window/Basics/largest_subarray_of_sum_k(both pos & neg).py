def largest_subarray_with_sum_k(arr, k):
    # Dictionary to store the prefix sum and its earliest index
    prefix_sum_map = {}
    sum_tot = 0  # Current prefix sum
    maxi = 0     # Maximum length of the subarray
    n = len(arr)

    for i in range(n):
        sum_tot += arr[i]  # Add the current element to the prefix sum

        # If the current sum is equal to k, update the maximum length
        if sum_tot == k:
            maxi = i + 1  # Subarray from the start to the current index

        # If the difference (sum_tot - k) exists in the map, it means we've found a subarray
        if (sum_tot - k) in prefix_sum_map:
            maxi = max(maxi, i - prefix_sum_map[sum_tot - k])

        # If the current prefix sum is not already in the map, store it with its index
        if sum_tot not in prefix_sum_map:
            prefix_sum_map[sum_tot] = i

    return maxi


arr = [4, 1, -1, 1, -1, 1, 2, 3, 5]
k = 5
print(largest_subarray_with_sum_k(arr, k))  # Output should be 5
