# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        curr_max=-float('inf')
        self.ans=0
        self.dfs(root,curr_max)
        return self.ans
    def dfs(self,root,curr_max):
        if not root:
            return
        if root.val>=curr_max:
            self.ans+=1
            curr_max=root.val
        self.dfs(root.left,curr_max)
        self.dfs(root.right,curr_max)
        return


