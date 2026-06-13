

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        # "Do I contain p or q in my subtree?"
        def dfs(node):
            if not node:
                return False

            # left  = did left subtree contain p or q?
            # right = did right subtree contain p or q?
            # cur   = am I p or q?
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node==p or node==q
            if (left and right) or (cur and right) or (cur and left):
                self.ans = node
                return
            return left or right or cur
        dfs(root)
        return self.ans