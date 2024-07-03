def frequency(arr,n):
    for i in range(n):
        flag=False
        for j in range(i):
            if arr[i]==arr[j]:
                flag=True
                break
        if flag==True:
            continue
        freq=1
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                freq+=1
        print(arr[i],freq)
def frequency2(arr,n):
    hmp=dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1
        else:
            hmp[arr[i]]=1
    for x in hmp:
        print(x," ",hmp[x])

l=[10,10,10,10,2,2,2,2,2,2,1,1,1,1,1,1,1,1,0,1]
frequency2(l,len(l))
