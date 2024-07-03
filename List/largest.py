def greatest(l):
    res=l[0]
    for i in range(1,len(l)):
        if l[i]>res:
            res=l[i]
    return res
def greatest2(l):
    for x in l:
        for y in l:
            if y>x:
                break
        else:
            return x
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8,9,10,11,2,25,41,89,85,68,58,56,70]
    print(greatest(l))
    print(greatest2(l))
