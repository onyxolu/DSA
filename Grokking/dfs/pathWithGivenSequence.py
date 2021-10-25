# Time Complexity = 0(N) => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes 
# LogN for trackback for leafnodes

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def pathsWithSequence(self, root, sequence):
        if not root:
            return len(sequence) == 0
        return self.findSequence(root, sequence, 0)

    def findSequence(self, node, sequence, sq_index):
        if node is None:
            return False

        sq_len = len(sequence)

        if sq_index >= sq_len or node.val != sequence[sq_index]:
            return False

        if node.left is None and node.right is None and sq_index == sq_len - 1:
            return True

        return self.findSequence(node.left, sequence, sq_index + 1) or self.findSequence(node.right, sequence, sq_index + 1)

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(root.pathsWithSequence(root, [1,9,2]))
    