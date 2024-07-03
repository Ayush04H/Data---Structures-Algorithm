def alldiv(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

def alldiv2(n):
    i=1
    while(i*i<n):
        if n%i == 0:
            print(i)
            if (i!=(n/i)):
                print(n//i)
        i+=i

def alldiv3(n):
    i=1
    while(i*i<n):
        if n%i == 0:
            print(i)
        i+=1
    while(i>=1):
        if n%i == 0:
            print(n//i)
        i-=1

if __name__=='__main__':
    print("For div1")
    alldiv(10)
    print("For div2")
    alldiv2(100)
    print("For div3")
    alldiv3(100)