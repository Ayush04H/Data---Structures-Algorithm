def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def pfactor(n):
    for i in range(2,n+1):
        if prime(i):
            x=i
            while n%x==0:
                print(i)
                x*=i

if __name__=='__main__':
    n=int(input("Enter the Number- "))
    pfactor(n)
