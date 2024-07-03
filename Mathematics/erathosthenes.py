def prime(n):
    if n == 1 :
        return False
        
    if n == 2 or n == 3 :
        return True
        
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    i = 5
    while (i * i <= n) :
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
        
def era(n):
    for i in range(2,n+1):
        if prime(i):
            print(i,end=" ")

def seive(n):
    if n<=1:
        return
    isprime=[True]* (n+1)
    i=2
    while i*i<=n:
        if isprime[i]:
            for j in range(2*i,n+1,i):
                isprime[j]=False
        i+=1
    for i in range(2,n+1):
        if isprime[i]:
            print(i,end=" ")
if __name__=='__main__':
    print("Naive Way")
    era(23)
    print("Efficient way")
    seive(23)
