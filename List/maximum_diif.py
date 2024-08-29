def max_d(l):
    max_diff=l[1]-l[0]
    min_val=l[0]
    for i in range(1,len(l)-1):
        max_diff=max(max_diff,l[i]-min_val)
        min_val=min(min_val,arr[i])
    return max_diff



arr=[2,3,10,6,4,8,1]
print(max_d(arr))