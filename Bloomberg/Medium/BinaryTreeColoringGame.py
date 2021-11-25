
# DFS

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Algorithm
# Find X = number of left nodes, right nodes and parent nodes
# Find best stratey to win which is to place y close to x outside x-left,right and parent




class Solution:
    def btreeGameWinningMove(self, root, n: int, x: int) -> bool:
        def countNode(cur):
            if not cur:
                return 0
            
            left = countNode(cur.left)
            right = countNode(cur.right)
            
            return left + right + 1
        
        def findX(cur):
            nonlocal left_nodes, right_nodes
            if not cur:
                return
            
            if cur.val == x:
                left_nodes = countNode(cur.left)
                right_nodes = countNode(cur.right)
                return
            
            left = findX(cur.left)
            right = findX(cur.right)
            
        left_nodes = right_nodes = parent_nodes = 0
        
        findX(root)
        
        parent_nodes = n - left_nodes - right_nodes - 1
        
        return max(left_nodes, right_nodes, parent_nodes) > n/2