'''
   1
  22
 333
4444
'''

def func(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=n-i:
                print(" ",end="")

            else:
                print(i,end="")

        print()


func(4)