def sumdig(n):
    s=0
    if n<10:
        return n 
    return sumdig(n//10)+(n%10)
n=1234
print(sumdig(n))
    