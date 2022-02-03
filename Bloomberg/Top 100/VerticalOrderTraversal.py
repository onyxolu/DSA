

# sort these nodes by their values
# BFS

# Stack and DefaultDict
# Time = 0(N) + KNLog(K)  K is no of columns
# Space = 0(NK)


class Solution:
    def verticalTraversal(self, root):
        
        from collections import defaultdict, deque

        Q = deque([(root, 0, 0)])
        distMap = defaultdict(list)

        while len(Q) > 0:
            size = len(Q)
            for _ in range(size):
                node, x, y = Q.popleft()

                #store y as key and x,val as tuple
                distMap[y].append((x, node.val))

                if node.left != None:
                    Q.append((node.left, x + 1, y - 1))

                if node.right != None:
                    Q.append((node.right, x + 1, y + 1))

        vertical = []
        minDist = min(distMap)
        maxDist = max(distMap)

        for dist in range(minDist, maxDist + 1):
            # sort by value
            vals = sorted(distMap[dist], key=lambda e: (e[0], e[1]))
            vertical.append([e[1] for e in vals])
            
        return vertical


# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        result = []
        if root == None: return result
        cache = {}
        self.minC, self.maxC = 0, 0
        
        def dfs(node, r, c):
            if node == None: return
            if c in cache: cache[c].append([r, node.val])
            else: cache[c] = [[r, node.val]]
            self.minC = min(self.minC, c)
            self.maxC = max(self.maxC, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
        
        dfs(root, 0, 0)
        for c in range(self.minC, self.maxC+1):
            col = sorted(cache[c], key = lambda x: (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)
            
        return result



