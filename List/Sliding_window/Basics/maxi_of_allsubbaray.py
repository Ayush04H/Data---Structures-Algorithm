from collections import deque

'''def max_of_subarray(arr, k):
    n = len(arr)
    
    # Loop through each subarray of size k
    for i in range(n - k + 1):
        # Initialize the maximum element in the current window
        current_max = arr[i]
        
        # Find the maximum in the current subarray
        for j in range(i + 1, i + k):
            current_max = max(current_max, arr[j])
        
        # Print the maximum of the current subarray
        print(current_max)  # Brute Force '''


def max_of_subarray(arr,k):
    i = 0
    j = 0
    n = len(arr)

    res =[]

    dq = deque()

    while j < n:
        while dq and arr[dq[-1]] < arr[j]:
            dq.pop()

        dq.append(j)

        if j-i+1 < k: 
            j+=1

        elif j-i+1 == k:
            res.append(arr[dq[0]])

            if dq[0] == i:
                dq.popleft()

            i+=1
            j+=1


    return res
arr = [1,3,-1,-3,5,3,6,7]
n = len(arr)
k = 3

print(max_of_subarray(arr,k))

