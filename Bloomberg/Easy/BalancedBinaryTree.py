# dfs - Post Order

class BinaryTree:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, root):
        def dfs(root):
            # Base Case
            if not root:
                return [True, 0]
            
            # left and right Traversal
            left, right = dfs(root.left), dfs(root.right)

            # check if balanced and also check for the length

            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        # return the value at index 0
        return dfs(root)[0]