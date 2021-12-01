
from collections import List

# Normal Matrix multiplication => row * Col
# 2by3 * 3by3 => 2by3

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rowA, colA = len(mat1), len(mat1[0])
        colB = len(mat2[0])
        # 2by3 * 3by3 => 2by3
        # row is from A, Column is from B
        
        ans = [[0] * colB for _ in range(rowA)] # row * col
        for i in range(rowA):
            for j in range(colB):
                ans[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(colA)])
        return ans
        
        
        