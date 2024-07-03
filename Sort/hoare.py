def hoare(a,l,h):
    pivot=a[l]
    i=l-1
    j=h+1
    while True:
        i+=1
        while a[i]<pivot:
            i+=1
        j-=1
        while a[j]>pivot:
            j-=1
        if i>=j:
            return j
        a[i],a[j]=a[j],a[i]

a=[5,3,8,4,2,7,1,10]
hoare(a,0,len(a)-1)
print(a)
