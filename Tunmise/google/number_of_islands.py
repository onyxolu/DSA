class Solution:
            
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    islands += 1
                    self.makeWater(grid,i,j)
        return islands
    
    def makeWater(self,grid,i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        else:
            
            grid[i][j] = "#"
            
            self.makeWater(grid,i-1,j)
            self.makeWater(grid,i,j-1)
            self.makeWater(grid,i,j+1)
            self.makeWater(grid,i+1,j)