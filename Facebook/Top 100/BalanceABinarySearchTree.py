from collections import TreeNode

# first do an inorder traversal and store in array
# Then build the tree with Binary search
            # root = TreeNode(arr[mid])
            # root.left = buildTree(lo, mid - 1)
            # root.right = buildTree(mid+1, hi)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inOrder(rt = root):
            nonlocal arr
            # base case
            if not rt: return
            
            # call left
            inOrder(rt.left)
            
            # process root
            arr.append(rt.val)
            
            # call right
            inOrder(rt.right)
        
        # get a sorted list of tree values
        inOrder()
        
        # construct the tree by recursively finding the median
        def buildTree(lo = 0, hi = len(arr) - 1):
            nonlocal arr
            # base case
            if lo > hi: return None
            if lo == hi: return TreeNode(arr[lo])
            
            # find the median
            mid = (lo + hi) // 2 # edge case: mid == lo
            rt = TreeNode(arr[mid])
            rt.left = buildTree(lo, mid - 1)
            rt.right = buildTree(mid+1, hi)
            return rt
        
        return buildTree()


# Iterative

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # DFS
        stack = []
        value = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                value.append(root.val)
                root = root.right
            else:
                break
				
        # Create Balanced Tree
        root = TreeNode(0)
        stack = [(root, 0, len(value))]
        while stack:
            cur, left, right = stack.pop(0)
            mid = (left + right) // 2
            cur.val = value[mid]
            if mid < right - 1:
                cur.right = TreeNode(0)
                stack.append((cur.right, mid+1, right))
            if left < mid:
                cur.left = TreeNode(0)
                stack.append((cur.left, left, mid))
        return root