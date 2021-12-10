

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix) -> int:
        # bottle neck - 1000 calls
        # Brute Force - 0(nm) check every row in column
        # Optimal - Two pointers with binary search on each row
        # 0000000
        # 0001000   3
        # 0110010  1
        # 0010011  2 ans = 1
        
        #to get the rows and cols, we need to call binary matrix
        rows, cols = binaryMatrix.dimensions()
        minCol = float("inf")
        
        #loop through rows
        for r in range(rows):
            left = 0
            right = cols - 1
            # binary search
            while left <= right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(r, mid) == 1:
                    minCol = min(minCol, mid)
                    right = mid - 1
                else:
                    left = mid + 1
                
        
        return minCol if minCol != float("inf") else -1
        