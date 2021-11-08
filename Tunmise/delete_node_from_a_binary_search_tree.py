# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root  = None
                return temp
            
                
            temp = self.minValNode(root.right)
            
            root.val = temp.val
            
            root.right = self.deleteNode(root.right,temp.val)
        return root
        
    def minValNode(self,root):
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr