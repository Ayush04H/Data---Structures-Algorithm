def sumdig(n):
    s=0
    if n<10:
        return 1
    return sumdig(n//10)+1
n=99999
print(sumdig(n))
    