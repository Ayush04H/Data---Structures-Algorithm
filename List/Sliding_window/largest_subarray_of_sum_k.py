def largest_subarray(arr, k):
    maxi = 0
    sum_tot = 0
    i = 0
    n = len(arr)

    for j in range(n):
        sum_tot += arr[j]

        # Shrink the window as long as the current sum exceeds k
        while sum_tot > k:
            sum_tot -= arr[i]
            i += 1

        # Check if we have found a subarray with sum exactly equal to k
        if sum_tot == k:
            maxi = max(maxi, j - i + 1)

    return maxi


arr = [4, 1, 1, 1,1,1, 2, 3, 5]
k = 5
print(largest_subarray(arr, k))  # Output should be 4
