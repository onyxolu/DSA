
from collections import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        
        for r in range(1,row):
            for c in range(1, col):
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True
    
    
    
    
#         if not matrix:
#             return False
        
#         diagonalVal = matrix[0][0]
#         row, col = len(matrix), len(matrix[0])
        
#         for r in range(row):
#             print(r, len(matrix[r]))
#             if not ( matrix[r] and matrix[r][r] == diagonalVal):
#                 return False
            
#         return True

        