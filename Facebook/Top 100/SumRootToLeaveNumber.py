

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def pathSum(node, pSum):
            if node is None:
                return 0
            pSum = 10 * pSum + node.val
            
            if node.left is None and node.right is None:
                return pSum
            
            return pathSum(node.left, pSum) + pathSum(node.right, pSum)
        
        return pathSum(root, 0)
        