class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += (4 - self.numOfNeighbors(grid,i,j))
        return perimeter
    
    def numOfNeighbors(self,grid,i,j):
        count = 0
        
        #up
        if i > 0 and grid[i-1][j] == 1:
            count += 1
        
        #left
        if j > 0 and grid[i][j-1] == 1:
            count += 1
        
        #down
        if i < len(grid) -1 and grid[i+1][j] == 1:
            count += 1
        
        #right
        if j < len(grid[0])-1 and grid[i][j+1] == 1:
            count += 1
        
        return count
        