

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root) :
        # DFS
        # Bottom Up Post ordertraversal
        def getDeepestlvl(node, level):
            nonlocal ans, deepest_lvl
            deepest_lvl = max(deepest_lvl, level)
            
            if not node:
                return level
            
            left_lvl = getDeepestlvl(node.left, level+1)
            right_lvl = getDeepestlvl(node.right, level+1)
            
            if left_lvl == right_lvl == deepest_lvl:
                ans = node
                
            return max(left_lvl, right_lvl)
        
        
        deepest_lvl = 0
        ans = None
        getDeepestlvl(root, 0)
        
        return ans
        