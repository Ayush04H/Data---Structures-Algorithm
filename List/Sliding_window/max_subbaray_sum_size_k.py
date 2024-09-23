def max_subbaray_sum(arr,k):
        n=len(arr)
        i,j = 0,0 
        sum_tot = 0
        maxi = float('-inf')
        
        while j < n:
            
            sum_tot += arr[j]
            if j-i+1 < k:
                j+=1
                
            elif j-i+1 == k:
                maxi = max(sum_tot,maxi)
                sum_tot -= arr[i]
                
                i+=1
                j+=1
                
        return maxi


Arr = [100, 200, 300, 400]
k=2

print(max_subbaray_sum(Arr,k))

