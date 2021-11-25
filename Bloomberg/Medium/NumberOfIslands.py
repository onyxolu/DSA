

# time complexity is O( n x m ) as you iterate through all elements in the grid and visit them only once

from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft() # DFS chnage to pop (pop most recently added)
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and  #out of range
                       c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                            q.append((r,c))
                            visit.add((r,c))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
                
        

# Recursive dfs
class Solution:
    def numIslands(self, grid):
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(grid, i - 1, j)  # up
            dfs(grid, i + 1, j)  # down
            dfs(grid, i, j - 1)  # left
            dfs(grid, i, j + 1)  # right

        res = 0
        for i, iv in enumerate(grid):
            for j, jv in enumerate(grid[i]):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res