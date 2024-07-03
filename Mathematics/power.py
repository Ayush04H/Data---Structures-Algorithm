def ispower(x,n):
    if n==0:
        print("1")
    else:
        res=1
        for i in range(1,n+1):
            res*=x
        print(res)

def ispower2(x, y):
    temp=0
    if y==0:
        return 1
    temp =ispower2(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x* temp * temp
     
def ispower3(x,n):
    res=1
    while n>0:
        if n%2!=0:
            res*=x
        x=x*x
        n=n//2

    return res

if __name__=='__main__':
    ispower(3,4)
    print(ispower2(3,3))
    print(ispower3(3,2))