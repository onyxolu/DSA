

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        # Bottom Up Recursion => 0(N)
        # for the height => 1 + max(left, right)
        # for null node, height -1
        # for the diameter => 2 + left + right
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right) 
        
        dfs(root)
        return res[0]
            