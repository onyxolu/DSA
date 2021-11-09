
# Time => 0(N)
# Space => 0(H) => worst 0(N)

def flatten(root):
    def dfs(root):
        if not root:
            return None
        leftTail =  dfs(root.left)
        rightTail = dfs(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightTail or leftTail or root
    dfs(root)