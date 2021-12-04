
# DFS

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        
        def helper(node, output, low, high):

            if node.val >= low and node.val <= high:
                output += node.val
            if node.left and node.val >= low:
                output = helper(node.left,output,low,high)
            if node.right and node.val <= high:
                output = helper(node.right,output,low,high)

            return output 

        output = 0
        output = helper(root, output, low, high)
        return output



# BFS

from collections import deque
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        
        sum = 0
        if not root:
            return sum
        q = deque([root])
        while q:
            curNode = q.popleft()
            if curNode.val >= low and curNode.val <= high:
                sum += curNode.val
            if curNode.left and curNode.val > low:
                q.append(curNode.left)
            if curNode.right and curNode.val < high:
                q.append(curNode.right)
                
        return sum
