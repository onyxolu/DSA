
# Capture everything except the unsurrounded regions
# regions connected to the border ai'nt connected
# go through the border elements
# find a "0" and change all the "0s" to "ts"
# go through entire grid and change "0s" to "x"
# change the "ts" to "0s
# 
# TC - 0(NM)

# dfs

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def capture(r,c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "0"):
                return
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        # capture unsurrounded regions (o => t)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "0" and r in [0, rows-1] or c in [0, cols-1]):
                    capture(r,c)
        
        # capture the surrounded regions (0 => x)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "0":
                    board[r][c] = "X"
        
        # uncapture unsurrounded regions (t => 0)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "0"
                    