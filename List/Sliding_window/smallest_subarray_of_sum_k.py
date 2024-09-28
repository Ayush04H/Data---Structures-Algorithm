def minSubArrayLen(k: int, arr: list[int]) -> int:
        n = len(arr)
        mini = float('inf')
        i = 0 
        sum_tot = 0
        for j in range(n):
            sum_tot += arr[j]
            while sum_tot >= k:
                mini = min(mini,j-i+1)
                sum_tot -= arr[i]
                i += 1
        return mini if mini != float('inf') else 0



target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))
