
# DFS

# RUn DFS and keep track of every path
# create arr paths to store paths
# pass curentPath to dfs to append every path

from collections import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, currentPath, paths):
            currentPath += "->" + str(node.val)
            if not node.left and not node.right:
                paths.append(currentPath)
                return
            if node.left:
                dfs(node.left, currentPath, paths)
            if node.right:
                dfs(node.right, currentPath, paths)
                
                
        paths = []
        if not root:
            return paths
        currentPath = str(root.val)
        if not root.left and not root.right:
            paths.append(currentPath)
        if root.left:
            dfs(root.left, currentPath, paths)
        if root.right:
            dfs(root.right, currentPath, paths)
        return paths
    