'''
Intuition:

1. any diameter in a tree will be calculated from left and right height .

2. so we need to calculate height for the nodes to tell it's diamter.

3. postorder pattern can help to start returning height from leaf level == base case == 0 height.

4. notice that in this type of pattern the info that we need from below node is height
of one side i.e. max which can be extended further up the tree.

5. diameter can be present anywhere across the tree so we need to compare every possible diameter in the tree.

6. Therefore we return height upwards but keep updating max diameter everytime.



Algorithm

1. Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
2. Implement a recursive function longestPath which takes a TreeNode as input. It should recursively explore the entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left and right branches:
    - if node is None, we have reached the end of the tree, hence we should return 0;
    - we want to recursively explore node's children, so we call longestPath again with node's left and right children. In return, we get the longest path of its left and right children leftPath and rightPath;
    - if leftPath plus rightPath is longer than the current longest diameter found, then we need to update diameter;
    - finally, we return the longer one of leftPath and rightPath. Remember to add 11 as the edge connecting it with its parent.
3. Call longestPath with root.



N is the number of nodes in the tree.

Time complexity - O(N) - This is because in our recursion function longestPath, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

Space complexity - O(N) - The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(Nlog N).
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter