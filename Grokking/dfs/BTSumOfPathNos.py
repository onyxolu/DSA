# Time Complexity = 0(N) => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes 
# LogN for trackback for leafnodes

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def pathNos(self, root):
        return self.getPathSum(root, 0)

    def getPathSum(self, currentNode, pathSum):
        if currentNode is None:
            return 0

        pathSum = 10 * pathSum + currentNode.val

        if currentNode.left is None and currentNode.right is None:
            return pathSum
        
        print(pathSum, "pathsum")
        return self.getPathSum(currentNode.left , pathSum) + self.getPathSum(currentNode.right, pathSum)

        

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print(root.pathNos(root))