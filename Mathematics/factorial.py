#iterative way
def fact(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res

#recuursive way
def fact2(n):
    if n==0:
        return 1
    return n * fact2(n-1)

if __name__ == '__main__':
    n=int(input("Enter the Number-"))
    print(fact(n))
    print(fact2(n))