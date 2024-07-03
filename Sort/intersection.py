def intrsection(a,b,m,n):
    for i in range(m):
        if (i>0 and a[i]==a[i-1]):
            continue
        for j in range(n):
            if(a[i]==b[j]):
                print(a[i],end=" ")
                break
a=[1,4,9,9,9,9,9,9,9,9,9,9,9,9,99,10]
b=[2,3,4,4,4,4,5,6,7,8,9,10,99]
intrsection(a,b,len(a),len(b))