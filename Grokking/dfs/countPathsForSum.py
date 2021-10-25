# Time Complexity = 0(N2) - worst     0(NLogN) balanced tree => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes 
# LogN for trackback for leafnodes

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def pathsForSum(self, root, S):
        return self.countPath(root, S, [])

    def countPath(self, node, S, currentPath):
        if node is None:
            return 0

        currentPath.append(node.val)

        pathCount, pathSum = 0,0

        for i in reversed(range(len(currentPath))):
            pathSum += currentPath[i]
            if pathSum == S:
                pathCount += 1

        pathCount += self.countPath(node.left, S, currentPath)
        pathCount += self.countPath(node.right, S, currentPath)

        del currentPath[-1]

        return pathCount
        

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)

print(root.pathsForSum(root, 12))