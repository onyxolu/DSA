def getViablePath(m,r,c):
    viablePaths = []
    for nr,nc in [(r,c+1),(r,c-1),(r-1,c),(r+1, c)]:
        if 0 <= nr < len(m) and 0 <= nc < len(m[0]) and m[nr][nc] != -1:
            viablePaths.append((nr,nc))
    return viablePaths


def bfs(grid, i,  j,x, y,visited):
    import collections
    if not grid:
        return []
    q = collections.deque()
    visited.add((i,j))
    q.append([i,j])

    while q:
        r,c = q.popleft()
        if (r,c) == (x,y):
            return True
        for nr,nc in getViablePath(grid,r,c):
            if (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append([nr,nc])
    return False

def ifZerosToEnd(matrix,er,ec):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if not bfs(matrix,i,j,er,ec,set()):
                    return False
    return True

def pathFromSourceToTarget(m,sr,sc,er,ec):
    start = (sr,sc)
    end = (er,ec)
    path = [start]
    visited =set()
    visited.add(start)

    pathSoFar = []
    

    def dfsUtil(source,dest,m,path,visited):
        if path[-1] == dest:
        
            pathSoFar.append(path)
            return
        
        for nr,nc in getViablePath(m,path[-1][0],path[-1][1]):
            edge = (nr,nc)
            if edge not in visited:
                visited.add(edge)
                dfsUtil(edge,dest,m,path+[edge],visited)
    
                visited.remove(edge)

    dfsUtil(start,end,m,path,visited)
    
    return pathSoFar
def getNumberOf1s(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                count += 1
    return count
m = [
    [0,0,1,0,0,0],
    [1,0,-1,0,-1,0],
    [0,-1,0,0,0,0],
    [0,-1,-1,1,-1,-1],
    [0,0,0,0,0,0]]
def shortestPath(m,sr,sc,er,ec):
    numberOf1s = getNumberOf1s(m)
    allPaths = pathFromSourceToTarget(m,sr,sc,er,ec)
    pathsTreasureCounts = []
    for i in range(len(allPaths)):
        count = 0
        for coord in allPaths[i]:
            if m[coord[0]][coord[1]] == 1:
                count += 1
        if count == numberOf1s:
            pathsTreasureCounts.append(allPaths[i])
    if len(pathsTreasureCounts) == 1:
        return pathsTreasureCounts[0]
    else:
        shortest = pathsTreasureCounts[0]
        min_index=0
        for i in range(1,len(pathsTreasureCounts)):
            if len(pathsTreasureCounts[i]) <= len(shortest):
                shortest = pathsTreasureCounts[i]
                min_index = i


        return pathsTreasureCounts[min_index]
    print(pathsTreasureCounts)

def shortestPathIfMax1sIsTheCase(m,sr,sc,er,ec):
    allPaths = pathFromSourceToTarget(m,sr,sc,er,ec)
    pathsTreasureCounts = []
    max_1 = float('-inf')
    for path in allPaths:
        count = 0
        for coord in path:
            if m[coord[0]][coord[1]] == 1:
                count += 1
        max_1 = max(max_1,count)
        pathsTreasureCounts.append(count)

    res = []
    for i, treasures in enumerate(pathsTreasureCounts):
        if treasures == max_1:
            res.append(allPaths[i])
    if len(res) == 1:
        return res[0]
    else:
        shortest = res[0]
        min_index=0
        for i in range(1,len(res)):
            if len(res[i]) <= len(shortest):
                shortest = res[i]
                min_index = i


        return res[min_index]
    
        


m2 = [[0,-1],[-1,-1]]
# print(getViablePath(m,4,3))
# print(ifZerosToEnd(m2,1,1))
# print(pathFromSourceToTarget(m,4,3,0,0))
print(shortestPathIfMax1sIsTheCase(m,4,3,0,0))
# print
