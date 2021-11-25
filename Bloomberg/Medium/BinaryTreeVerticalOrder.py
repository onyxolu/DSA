
#left to right

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root):
        
        from collections import defaultdict, deque
        
        if not root:
            return []

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
            vals = sorted(distMap[dist], key=lambda e: (e[0]))
            vertical.append([e[1] for e in vals])
            
        return vertical
        