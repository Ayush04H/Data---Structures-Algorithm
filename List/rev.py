def revl(l):
    return l.reverse()
def revl2(l):
    s=0
    e=len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1
if __name__=='__main__':
    l=[1,2,3,5,21,62,8]
    revl2(l)
    print(l)
    l2=[1,2,3,5,21,62,8,998,56,23,78,852]
    revl(l2)
    print(l2)
