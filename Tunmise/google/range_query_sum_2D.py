class NumMatrix:

    def __init__(self, matrix):
        self.rows = len(matrix) + 1
        self.cols = len(matrix[0]) + 1
        self.prefsum = p = [[0] * self.cols for i in range(self.rows)]
        
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefsum
        row2 += 1
        col2 += 1
        return p[row2][col2] - p[row2][col1] - p[row1][col2] + p[row1][col1]