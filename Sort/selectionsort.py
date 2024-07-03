def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if l[j]<l[min_ind]:
                min_ind=j
        l[min_ind],l[i]=l[i],l[min_ind]
l=[10,8,20,5,110,0,63,87,12,11]
selectionsort(l)
print(l)