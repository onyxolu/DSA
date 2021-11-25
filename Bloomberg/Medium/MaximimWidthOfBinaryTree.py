# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
                    
    
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        max_width = 0
        q = deque([(root, 0)])
        while q:
            length = len(q)
            win = []
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            for _ in range(length):
                node, x = q.popleft()
                if node.left:
                    q.append((node.left, 2 * x)) # Add node and index
                if node.right:
                    q.append((node.right, 2 * x + 1))
            
        return max_width
            
                