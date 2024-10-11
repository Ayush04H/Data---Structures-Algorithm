def longest_greater(arr,k):
    max_len = 0
    sum_tot = 0 
    res = []
    i = j = 0
    n = len(arr)

    while j < n:
        sum_tot += arr[j]

        while sum_tot < k and i <= j :
            sum_tot -= arr[i]
            i += 1

        if sum_tot > k:
            if j-i+1 > max_len:
                max_len = j-i+1
                res = arr[i:j+1]

        j+=1

    return max_len,res 


arr = [1, 2, 3, 1, -1, 3, 5, 2]
max_len , res = longest_greater(arr,10)
print('Size of the array is ',max_len)
print('The Subarray is ',res)
