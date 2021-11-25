


# Solution one - Inorder Traversal and store vals in array

class Solution:
    def inorderSuccessor(self, root, p):
        if not root: return
        inorder = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
        dfs(root)
        inorder.append(None)
        for i in range(len(inorder)):
            if inorder[i] == p: return inorder[i+1]


# Step 2: optimal - BST Property - Binary Search
# Time - 0(logN) or 0(Height)
    
class Solution:
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor