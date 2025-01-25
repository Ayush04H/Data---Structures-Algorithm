def sum_recc(n):
    s=0
    if n<10:
        return n 
    return sum_recc(n//10)+(n%10)
n=1234
print(sum_recc(n))
    