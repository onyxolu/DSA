
# log(N)


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def closestValue(self, root, target: float) -> int:
        if not root:
            return -1

        result = (float('inf'), float('inf'))
        while root:
            diff = abs(target-root.val)
            if diff < result[1]:
                result = (root.val, diff)
            
            if target > root.val:
                root = root.right
            elif target < root.val:
                root = root.left
            elif target == root.val:
                return root.val
        return result[0]
        