def merge(a,b):
    res=a+b
    res.sort()
    return res

def merge2(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
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
print(merge2(a,b))
