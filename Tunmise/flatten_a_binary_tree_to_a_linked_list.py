class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flatten(node):
            if not node: return
            
            # leaf node
            if not node.left and not node.right:
                return node
            
            left  = flatten(node.left)
            right = flatten(node.right)
            
            # If there was a left subtree, we shuffle the connections
            # around so that there is nothing on the left side
            # anymore.
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            
            # we need to return the rightmost node
            return right if right else left
        
        flatten(root)