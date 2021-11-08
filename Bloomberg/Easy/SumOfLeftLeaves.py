
# Time Complexity = 0(N) => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes 

# BFS

from collections import deque

def sumOfLeftLeaves(self, root):
    if root.left is None and root.right is None:
        return 0
    result = 0
    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        if currentNode.left:
            queue.append(currentNode.left)
            if currentNode.left.left is None and currentNode.left.right is None:
                result += currentNode.left.val
        if currentNode.right:
            queue.append(currentNode.right)
            
    return result
