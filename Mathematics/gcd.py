#eucledin approach
def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
    
def gcd2(a,b):

    if b==0:
        return a
    return gcd2(b,a%b)
    
if __name__ == '__main__':
    a=21
    b=7
    print(gcd(a,b))
    print(gcd2(a,b))