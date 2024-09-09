def eggDrop(n, k):
        # code here
        t = [0 for i in range(n+1)]
        m = 0
        while t[n] < k:
            m+=1
            for i in range(n,0,-1):
                t[i] += 1 + t[i-1]
            
        return m

e=3 
f=5 
print(eggDrop(e,f))