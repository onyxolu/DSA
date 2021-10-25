

# Time Complexity = 0(N) => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes

class TreeNode:
    def __init__(self , val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def has_path(self, node, targetSum):
        # check for leave node
        if node is None:
            return False

        if node.val == targetSum and node.right is None and node.left is None:
            return True

        return self.has_path(node.left, targetSum - node.val) or self.has_path(node.right, targetSum - node.val)

    
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(root.has_path(root,18))

main()

