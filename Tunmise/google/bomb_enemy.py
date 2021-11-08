class Solution:
    
    def maxKilledEnemies(self, grid):
        
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        
        north = [[0 for _ in range(n)] for _ in range(m)]
        west = [[0 for _ in range(n)] for _ in range(m)]
        south = [[0 for _ in range(n)] for _ in range(m)]
        east = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] is 'W':
                    continue
                if grid[i][j] is 'E':
                    north[i][j] += 1 
                    west[i][j] += 1
                if i > 0:
                    north[i][j] += north[i-1][j]
                if j > 0:
                    west[i][j] += west[i][j-1]
                    
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] is 'W':
                    continue
                if grid[i][j] is 'E':
                    south[i][j] += 1 
                    east[i][j] += 1 
                if i + 1 < m:
                    south[i][j] += south[i+1][j]
                if j + 1 < n:
                    east[i][j] += east[i][j+1]
                    
        max_kills = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] is '0':
                    kills = north[i][j] + west[i][j] + south[i][j] + east[i][j]
                    max_kills = max(max_kills, kills)
                    
        return max_kills


class Solution:
    def maxKilledEnemies(self, grid):
        # init
        if not grid or len(grid) == 0 or len(grid[0]) == 0 :
            return 0
        row, col = len(grid), len(grid[0])
        # init
        up = [[0] * col for _ in range(row)]
        down = [[0] * col for _ in range(row)]
        left = [[0] * col for _ in range(row)]
        right = [[0] * col for _ in range(row)]
        # up
        for i in range(row) : 
            for j in range(col) :
                if grid[i][j] != 'W' :
                    if grid[i][j] == 'E' :
                        up[i][j] = 1
                    if i > 0 :
                        up[i][j] += up[i - 1][j]
        # down
        for i in range(row - 1, -1, -1) :
            for j in range(col) :
                if grid[i][j] != 'W' :
                    if grid[i][j] == 'E' :
                        down[i][j] = 1
                    if i + 1 < row :
                        down[i][j] += down[i + 1][j]
        # right
        for i in range(row) : 
            for j in range(col - 1, -1, -1) :
                if grid[i][j] != 'W' :
                    if grid[i][j] == 'E' :
                        right[i][j] = 1
                    if j + 1 < col :
                        right[i][j] += right[i][j + 1]
                        
        # left
        for i in range(row) : 
            for j in range(col) :
                if grid[i][j] != 'W' :
                    if grid[i][j] == 'E' :
                        left[i][j] = 1
                    if j > 0 :
                        left[i][j] += left[i][j - 1]
        
        # sum 
        res = 0
        for i in range(row):
            for j in range(col) :
                if grid[i][j] == '0' :
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        
        return res