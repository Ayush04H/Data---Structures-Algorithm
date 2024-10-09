def genereate_subarray(arr):
    n = len(arr)
    subarrays = []
    for i in range(n):
        for j in range(i,n):
            subarrays.append(arr[i:j+1])

    return subarrays


def longest_less_than_k(arr,k):
    subarrays = genereate_subarray(arr)
    max_len = 0 
    res = []
    for subarray in subarrays:
        if sum(subarray) <  k:
            if len(subarray) > max_len:
                max_len = len(subarray)
                res = subarray

    return max_len , res 


arr = [1, 2, 3, 1, -1, 3, 5, 2]
# print(genereate_subarray(arr))
max_len , res = longest_less_than_k(arr,10)
print('Size of the array is ',max_len)
print('The Subarray is ',res)