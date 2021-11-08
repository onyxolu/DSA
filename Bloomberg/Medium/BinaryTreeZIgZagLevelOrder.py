

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        zigzagCheck = False
        while queue:
            levelSize = len(queue)
            currentLevel = deque()
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if zigzagCheck:
                    currentLevel.appendleft(currentNode.val)
                else: 
                    currentLevel.append(currentNode.val)
                    
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(currentLevel)
            zigzagCheck = not zigzagCheck
        return result