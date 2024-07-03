#sum
def issum(x):
    res=x*(x+1)//2
    return res
#palli
def palli(n):
    temp=n
    rv=0
    while temp!=0:
        id=temp%10
        rv=(rv*10)+id
        temp=temp//10
    return rv==n
#cntdigits
def cntdigits(n):
    res=0
    while n!=0:
        n//=10
        res+=1
    return res
#fac
def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
#gcd
def gcd(a,b):

    if b==0:
        return a
    return gcd(b,a%b)
#lcm
def lcm(a,b):

    return (a*b)//gcd(a,b)
#prime
def isprime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
#primefact
def pfactor(n):
   for i in range(2,n+1):
        if isprime(i):
            x=i
            while n%x==0:
                print(i)
                x*=i

#alldiv
def alldiv(n):
    i=1
    while (i*i<n):
        if n%i==0:
            print(i)
        i+=1
    while (i>=1):
        if n%i==0:
            print(n//i)
        i-=1
#erathosthnes
def era(n):
    for i in range(1,n+1):
        if isprime(i):
            print(i,end=" ")
#power
def poww(x,n):
    res=1
    while n>0:
        if n&1:
            res*=x
        x=x*x
        n=n>>1
    return res
if __name__ == '__main__':

    print(alldiv(100))
    print(era(100))
    print(poww(12,2))