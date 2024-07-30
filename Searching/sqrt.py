def sqrtfloor(x):
    i=1
    while i*i<=x:
        i+=1
    return i-1
def sqrtfloor2(n):
    low=1 
    high=n 
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        msq=mid*mid
        if(msq==n):
            return mid
        elif (msq>n):
            high=mid-1
        else:
            low=mid+1 
            ans=mid 
    return ans
print(sqrtfloor2(8))