def max_subarray(arr):
    res=arr[0]
    max_end=arr[0]
    for i in range(1,len(arr)):
        max_end=max(max_end+arr[i],arr[i])
        res=max(res,max_end)
    return res

arr=[-6,-1,-8]
print(max_subarray(arr))