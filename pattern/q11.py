'''
12345
1234
123
12
1

'''
def func(n:int):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")

        print("")


func(5)