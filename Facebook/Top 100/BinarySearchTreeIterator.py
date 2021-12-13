
# Inorder Traversal

from collections import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [] # store the leftmost nodes first
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left
        

    def next(self) -> int:
        ans = self.stack[-1].val
        cur = self.stack.pop()
        
        if cur.right: # check if it has right so we can add leftmost nodes
            cur = cur.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        return ans
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()