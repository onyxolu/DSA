class Solution(object): 
    def removeStones(self, stones):
        def dfs(x, y):
            seen.add((x, y))
            for new_y in groupX[x]:
                if (x, new_y) not in seen:
                    dfs(x, new_y)
            for new_x in groupY[y]:
                if (new_x, y) not in seen:
                    dfs(new_x, y)
                    
        seen = set ()
        island = 0
        groupX = collections.defaultdict(list)
        groupY = collections.defaultdict(list)
        
        #group the coordinates in the adjency list
        
        for x, y in stones:
            groupX[x].append(y)
            groupY[y].append(x)
        
            
        for (x, y) in stones:
            if (x, y) not in seen:
                dfs(x, y)
                island += 1
          
        return len(stones) - island