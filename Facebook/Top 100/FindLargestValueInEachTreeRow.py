# BFS


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            maxVal = float("-inf")
            for _ in range(qLen):
                curNode = q.popleft()
                maxVal = max(maxVal, curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            res.append(maxVal)
        return res