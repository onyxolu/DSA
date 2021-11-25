
# Time = 0(n*m*dfs) => 0(n*m * 4^len(word))
# Space = Call Stack len(word)

class Solution:
    def exist(self, board, word: str) -> bool:
        # Brute force 
        # find first character then check neighbours till we form word
        
        # Recursive Backtracking with DFS
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(r,c,i):
            # if we reach the end of the word
            if i == len(word): 
                return True
            # if we go out of bound
            if (r < 0 or c < 0 or r>= rows or c >= cols or word[i] != board[r][c] or (r,c) in visited):
                return False
                
            visited.add((r,c))
            res = (dfs(r+1, c, i+1) or 
                  dfs(r-1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r, c-1, i+1))
            visited.remove((r,c))
            return res
        
        # Go through every single position in grid and run dfs on it
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
                
        return False 