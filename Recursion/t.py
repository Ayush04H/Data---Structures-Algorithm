def f(x):
    if x>0:
        return x+f(x-2)
    else:
        return 0

print(f(10))