
# dfs is brute force sort of 0(mn)2 cos we will visit every node and for each node check for nearest gate 
# # bfs from gates (multiple sources)
# first find all the rooms 1 distance from the gate, then 2 then 3, continue till queue is empty

# Time => 0(mn)
# Space => 0(mn)

from collections import deque

class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def addRoom(r,c):
            if (r < 0 or r > rows-1 or c < 0 or c > cols-1 or (r,c) in visited or rooms[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])
            
        
        rows , cols = len(rooms), len(rooms[0])
        visited = set() #set of tuples
        q = deque()
        
        # find all the gates and put them in queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
                    
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                
                # some rooms might have been visited so we will use an helper function
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
                
            dist += 1 

