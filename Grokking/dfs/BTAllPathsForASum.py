# Time Complexity = 0(NLogN) => N is no of Nodes 
# Space Complexity = 0(NlogN) => N is no of Nodes 
# LogN for trackback for leafnodes

class TreeNode:
   def __init__(self, val, left = None, right = None):
       self.val = val
       self.left = left
       self.right = right

   def getAllPaths(self, root, targetSum):
       noOfPaths = []
       self.allPaths(root, targetSum, [], noOfPaths)
       return noOfPaths

   def allPaths(self, node, targetSum, currentPath, NoOfPaths):
        if node is None:
            return 

        currentPath.append(node.val)
        
        if node.val == targetSum and node.left is None and node.right is None:
            NoOfPaths.append(list(currentPath))
        else:
            self.allPaths(node.left, targetSum - node.val, currentPath, NoOfPaths) 
            self.allPaths(node.right, targetSum - node.val, currentPath, NoOfPaths)
        del currentPath[-1]

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.right = TreeNode(7)

print(root.getAllPaths(root, 12))