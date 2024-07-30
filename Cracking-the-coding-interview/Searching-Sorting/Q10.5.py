'''

The program performs a binary search on a sorted array interspersed with empty strings. 
It adjusts the search if the middle element is empty by finding the nearest non-empty string. 
This approach ensures efficient searching with 
𝑂(log𝑛)
O(logn) time complexity in the best case, but can degrade to 
𝑂(𝑛)
O(n) in the worst case due to many empty strings.

 Space complexity is  O(1).

'''

def find_string(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Find the nearest non-empty string if mid is empty
        if arr[mid] == "":
            l = mid - 1
            r = mid + 1
            while True:
                if l < left and r > right:
                    return -1
                elif r <= right and arr[r] != "":
                    mid = r
                    break
                elif l >= left and arr[l] != "":
                    mid = l
                    break
                r += 1
                l -= 1
        
        # Standard binary search
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test cases
arr1 = ["for", "geeks", "", "", "", "", "ide", "practice", "", "", "", "quiz"]
x1 = "quiz"
print(find_string(arr1, x1))  # Output: 1

x2 = "ide"
print(find_string(arr1, x2))  # Output: -1
