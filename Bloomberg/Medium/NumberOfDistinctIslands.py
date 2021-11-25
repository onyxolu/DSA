

class Solution:
    def numDistinctIslands(self, grid) -> int:
        seen = set()
        def dfs(r,c,r0,c0):
            if (0 <= r < len(grid) and 
                0 <= c < len(grid[0]) and 
                grid[r][c] and (r,c) not in seen):
                seen.add((r,c))
                shape.add((r - r0, c- c0))
                dfs(r+1, c, r0, c0)
                dfs(r-1, c, r0, c0)
                dfs(r, c+1, r0, c0)
                dfs(r, c-1, r0, c0)
                
        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                dfs(r,c,r,c)
                if shape:
                    shapes.add(frozenset(shape)) # frozenset takes an iterable object as input and makes them immutable
        return len(shapes)
        