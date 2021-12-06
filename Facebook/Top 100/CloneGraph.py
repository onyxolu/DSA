from collections import Node

# 0(n) => Edges + vertices
# Create copy nodes for each node
# use hashmap, map old nodes to copy(new) nodes to avoid duplicate nodes
# 

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        if not node:
            return None
        def dfs_clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
            return copy
        
        return dfs_clone(node)
        