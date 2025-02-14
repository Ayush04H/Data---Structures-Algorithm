'''
555555555
 4444444 
  33333  
   222   
    1    
'''

def func(n):
    for i in range(n,0,-1):
        for j in range(1,2*n):
            if j >= n-(i-1) and j <= n+(i-1):
                print(i,end="")
            else:
                print(" ",end="")

        print()


func(5)
