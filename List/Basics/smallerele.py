def smallr(l,x):
    l1=[]
    for i in range(0,len(l)):
        if l[i]<x:
            l1.append(l[i])
    return l1
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8,9,10,11,2,25,41,89,85,68,58,56,70]
    a=smallr(l,10)
    print(a)