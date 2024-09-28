def longestOnes(nums: list[int], k: int) -> int:
        max_cons = 0
        zero_cnt = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_cnt += 1

            while zero_cnt > k:
                if nums[i] == 0:
                    zero_cnt -=1

                i += 1

            max_cons = max(max_cons,j-i+1)


        return max_cons
    

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))




        