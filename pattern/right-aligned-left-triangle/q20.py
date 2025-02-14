'''
   A
  BB
 CCC
DDDD
'''

def func(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j<=n-i:
                print(" ",end="")

            else:
                print(chr(i+64),end="")

        print()


func(4)