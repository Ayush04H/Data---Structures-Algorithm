class InfiniteSizeArray:
    def __init__(self, arr):
        self._size = len(arr)
        self._arr = arr

    def readValueAtIndex(self, index):
        if index >= self._size:
            return 1000000007  # A large value representing infinity
        else:
            return self._arr[index]

def InfiniteSizeArray_search(obj, target):
    start, end = 0, 1
    
    # Increase the range exponentially until we find the range that includes the target
    while obj.readValueAtIndex(end) < target:
        start = end
        end *= 2
    
    # Perform binary search within the defined range
    while start <= end:
        mid = start + (end - start) // 2
        mid_val = obj.readValueAtIndex(mid)
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

# Testing the code
def test_infinite_array_search():
    array = [-1, 0, 3, 5, 9, 12, 85 , 56 ,21 , 69 , 2, 33 , 54, 68 ,89 ,741, 258 ,963, 123 ,456 ,7889 ,741 , 147 ,951]
    inf_array = InfiniteSizeArray(array)
    
    target = 9
    result = InfiniteSizeArray_search(inf_array, target)
    print(f"Index of target {target}: {result}")
    
    target = 9519
    result = InfiniteSizeArray_search(inf_array, target)
    print(f"Index of target {target}: {result}")

test_infinite_array_search()
