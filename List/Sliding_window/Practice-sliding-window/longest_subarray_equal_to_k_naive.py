def generate_subarray(arr):
    n = len(arr)
    subarrays = []
    for i in range(n):
        for j in range(i,n):
            subarrays.append(arr[i:j+1])

    return subarrays


arr = [1,2,3]
# print(generate_subarray(arr))
def longest_subarray_equal_k(arr,k):
    subarrays = generate_subarray(arr)
    max_len = 0
    res = []
    for subarray in subarrays:
        if sum(subarray) == k:
            if len(subarray) > max_len:
                max_len = len(subarray)
                res = subarray

    return max_len , res 

arr = [1, 2, 3, 1, -1, 3, 5, 2]
# print(generate_subarray(arr))

max_len , res = longest_subarray_equal_k(arr,10)
print('Size of the array is ',max_len)
print('The Subarray is ',res)

