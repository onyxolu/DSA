
# 1. Last Value in Postorder is Root
# 2. values before root in Inorder is left and values after root in Inorder is right
 
# Not so efficient => 0(n^2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        def dfs(inorder, postorder):
            if not inorder or not postorder:
                return None
            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)
            root.right = dfs(inorder[mid+1:], postorder)
            root.left = dfs(inorder[:mid], postorder)
            return root
        
        return dfs(inorder, postorder)


# 0(N)

class Solution:
    def buildTree(self, inorder, postorder):
        mapper = {}
        for i,v in enumerate(inorder):
            mapper[v] = i
            
        def dfs(low,high):
            if low > high:
                return
            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = dfs(mid+1, high)
            root.left = dfs(low, mid-1)
            return root
        
        return dfs(0, len(inorder)-1)