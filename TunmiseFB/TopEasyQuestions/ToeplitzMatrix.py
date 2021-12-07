'''
APPROACH: Compare With Top-Left Neighbor [Accepted]

Intuition and Algorithm

For each diagonal with elements in order a_1, a_2, a_3,...., a_k, we can check a_1 = a_2, a_2 = a_3,...., a_{k-1} = a_k. The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].

Time Complexity: O(M*N), as defined in the problem statement.

Space Complexity: O(1).

'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        
        for r in range(1,row):
            for c in range(1, col):
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True