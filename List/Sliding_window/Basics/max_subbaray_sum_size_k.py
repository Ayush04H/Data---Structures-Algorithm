'''
def max_sum_of_subarray(arr, n, k):
    max_sum = 0;
    for i in range(0, n-k+1):
        temp = 0;
        for j in range(i, i+k):
            temp += arr[j];

        if (temp > max_sum):
            max_sum = temp;

    return max_sum;


arr = [ 1, 4, 2, 10, 2, 3, 1, 0, 20 ];
k = 4;
n = len(arr);
max_sum=0;

 # brute force
max_sum = max_sum_of_subarray(arr, n, k);
print(max_sum);


Time:0(n^2)
Space:0(1)
'''


#Time:O(n)
#Space:O(1)

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


Arr = [1,2,3,4,5,6,1]
k=3

print(max_subbaray_sum(Arr,k))

