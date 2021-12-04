
from collections import Optional

# It is not a BST, so we cannot assume left is smaller than right
# we can do top down recursion (less code), and keep track of min and max we've seen so far and stop at leaf node
# 8,3,1  - min 1, max 8
# 8,3,6,4 - min 3, max 8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min
            
            # we update cur_min and cur_max
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            
            return max(dfs(node.left, cur_min, cur_max), dfs(node.right, cur_min, cur_max))
        return dfs(root, root.val, root.val)
        