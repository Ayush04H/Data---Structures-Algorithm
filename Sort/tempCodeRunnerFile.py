def lomoutopart(a,l,h):
    pivot=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    
    a[i+1],a[h]=a[h],a[i+1]
    return i+1

arr = [10, 80, 30, 90, 50, 70]
lomoutopart(arr,0,len(arr)-1)
print(arr)