'''
    1    
   121   
  12321  
 1234321 
123454321
'''

def func(n):
    # Upper triangle
    for i in range(1, n + 1):
        num = 1
        for j in range(1, 2 * n):
            if j >= n - (i - 1) and j <= n + (i - 1):
                print(num, end="")
                if j < n:
                    num += 1
                else:
                    num -= 1
            else:
                print(" ", end="")
        print()

func(5)
