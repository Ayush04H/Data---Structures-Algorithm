'''
Search in Sorted Rotated Array 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

'''

def rotatedsearch(l : list[int], x : int) -> int:
    low=0 
    high=len(l) - 1
    while low <= high:
        mid= (low + high)//2 
        if l[mid] == mid :
            return mid 
        if l[low] <= l[mid] :
            if l[low] <= x < l[mid] :
                high = mid -1 
            else:
                low = mid + 1 
        else:
            if l[mid] < x <= l[high] :
                low = mid + 1 
            else:
                high = mid -1

    return -1


""" 
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""