
from collections import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        # link node to parents
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        
        def get_values(target, k, curr_d, visited):
            if not target:
                return
            if target in visited:
                return
            if curr_d == k:
                ans.append(target.val)
                return
            visited.add(target)
            get_values(target.left, k, curr_d + 1, visited)
            get_values(target.right, k, curr_d + 1, visited)
            get_values(target.parent, k, curr_d + 1, visited)
        
        visited = set()
        get_values(target, k, 0, visited)
        return ans