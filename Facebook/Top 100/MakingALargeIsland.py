
# Union FInd

from collections import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # initialize union find data structure
        parents = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                parents[i][j] = (i, j)
        
        def find(i, j):
            if parents[i][j] != (i, j):
                parents[i][j] = find(parents[i][j][0], parents[i][j][1])
            return parents[i][j]
        
        def union(i, j, k, l):
            parent_x = find(i, j)
            parent_y = find(k, l)
            if parent_x != parent_y:
                parents[parent_x[0]][parent_x[1]] = parent_y
                
        # connect islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if i - 1 >= 0 and grid[i-1][j] == 1: union(i, j, i-1, j)
                    if j - 1 >= 0 and grid[i][j-1] == 1: union(i, j, i, j-1)
                        
        # create a hashmap of {parent index : size of island}
        island_size = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: continue
                par = find(i, j)
                if par not in island_size: island_size[par] = 1
                else: island_size[par] += 1
                    
        def get_size(i, j):
            nonlocal n
            islands = set([])
            siz = 1
            for ii, jj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if ii < 0 or ii >= n or jj < 0 or jj >= n: continue
                if grid[ii][jj] == 0: continue
                par = find(ii, jj)
                if par in islands: continue
                islands.add(par)
                siz += island_size[par] 
            return siz
                    
        # find current largest island
        if len(island_size) == 0: return 1
        max_island = max(island_size.values())
        
        # for each 0, check the island size if 0 is turned on
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    size = get_size(i, j)
                    if size > max_island:
                        max_island = size
                        
        return max_island
