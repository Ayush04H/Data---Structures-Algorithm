def reverse(l,s,e):

    while s<e:
        l[s],l[e] = l[e],l[s]
        s+=1
        e-=1

def leftrotated(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)



l=[1,2,3,4,5,6,7]
d=3
leftrotated(l, d)
print(l)


def rightrotated(l,d):
    n = len(l)
    d = d%n
    reverse(l,0,n-1)
    reverse(l,0,d-1)
    reverse(l,d,n-1)


l = [10, 20, 30, 40, 50]
d = 3
rightrotated(l, d)
print(l)