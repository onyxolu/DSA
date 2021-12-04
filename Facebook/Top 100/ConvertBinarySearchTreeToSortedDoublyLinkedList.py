from collections import Node

# Definition for a Node.
""""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # first analyze BST ppties
        # analye what a circular LL is as well
        # we need to do this inplace so we need to reassign pointers
        # from the example, we will need an inorder traversal(left, root and right)
        # easiest/cleanest way is dfs
        
        # we need head and tail pointer for linked list
        # will the linkedlist have prev/next or right and left?
        
        if not root:
            return 
        
        def dfs(node):
            nonlocal head, tail
            
            if not node:
                return
            dfs(node.left)
            
            # handle tail and head
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node
            
            tail = node
                
            dfs(node.right)
        
        head, tail = None, None
        dfs(root)
        head.left = tail
        tail.right = head
        
        return head