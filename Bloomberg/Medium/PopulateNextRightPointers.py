

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            prevNode = None
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if prevNode:
                    prevNode.next = currentNode
                prevNode = currentNode
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return root
        