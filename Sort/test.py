def merge(a,b):
    m=len(a)
    n=len(b)
    i=j=0
    res=[]
    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    
    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1


    return res


a=[1,6,7,8]
b=[2,3,4,5]
print(merge(a,b))

