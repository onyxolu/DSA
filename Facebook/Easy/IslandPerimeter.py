# Time Complexity => 0(N*M)


def islandPerimeter(grid):
    visit = set()

    def dfs(i,j):
        # Base case (Out of Bound)

        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0
        
        visit.add((i, j))
        perim = dfs(i, j+1)
        perim += dfs(i+1, j)
        perim += dfs(i, j-1)
        perim += dfs(i-1, j)
        return perim


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i,j)



print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))