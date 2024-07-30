# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Initialize start and end
        left, right = 0, 20000
        while left < right:
            mid = (left + right) >> 1
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
        
       
# Testing the code with a simulated ArrayReader
class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        if index >= len(self.array):
            return float('inf')
        return self.array[index]

# Function to test the Solution class
def test_solution():
    array = [-1, 0, 3, 5, 9, 12]
    reader = ArrayReader(array)
    solution = Solution()
    
    target = 9
    result = solution.search(reader, target)
    print(f"Index of target {target}: {result}")  # Expected output: 4
    
    target = 12
    result = solution.search(reader, target)
    print(f"Index of target {target}: {result}")  # Expected output: -1

test_solution()
