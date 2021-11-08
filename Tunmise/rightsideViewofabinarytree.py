# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root):
        d = defaultdict(list)
        res = []
        def helper(root,height):
            if root == None:
                return
            d[height].append(root.val)
            if root.right:
                helper(root.right,height+1)
            if root.left:
                helper(root.left,height+1)
            
        helper(root,0)
        
        for val in d.values():
            res.append(val[0])