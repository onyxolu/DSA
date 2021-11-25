
# 1. First Value in Preorder is Root
# 2. values before root in Inorder is left and values after root in Inorder is right

# Is every Value going to be unique?

# 0(n^2)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0(n^2)

class Solution:
    def buildTree(self, preorder, inorder):
    
        root = None
        
        if inorder and preorder:
            
            val = preorder[0]
            mid = inorder.index(val)
            root = TreeNode(val)
            
            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            
        return root



class Solution:
    def buildTree(self, preorder, inorder):
        mapper = {}
        for i,v in enumerate(inorder):
            mapper[v] = i

        root = None
        
        if inorder and preorder:
            
            val = preorder[0]
            mid = mapper[val]
            root = TreeNode(val)
            
            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            
        return root


# 0(N)
class Solution:
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        io_index = 0
        po_index = 1
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        while stack:
            current = stack[-1]
            
            while inorder[io_index] != current.val:
                current.left = TreeNode(preorder[po_index])
                current = current.left
                stack.append(current)
                po_index += 1
                
            while stack and inorder[io_index] == stack[-1].val:
                current = stack.pop()
                io_index += 1
            
            if po_index < n:
                current.right = TreeNode(preorder[po_index])
                stack.append(current.right)
                po_index += 1

        return root  
    
    