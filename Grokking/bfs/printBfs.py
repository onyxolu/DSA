
# Time Complexity = 0(N) => N is no of Nodes 
# Space Complexity = 0(N) => N is no of Nodes 

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


    def bfs_nolevel(self, root):
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            currentNode = queue.popleft()
            result.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return result

    def print_bfs(self, root):
        result = []
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            result.append(currentLevel)
        return result

    def zigzag_bfs(self, root):
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
            

    def bottom_up_bfs(self, root):
        result = deque()
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            currentLevel = []
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.appendleft(currentLevel)
        return result

    def avg_of_levels_bfs(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            levelSum = 0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelSum += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(levelSum/levelSize)
        return result

    def min_depth(self, root):
        result = 0
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            result += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                if not currentNode.left and not currentNode.right:
                    return result 

    def max_depth(self, root):
        result = 0
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            result += 1 
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return result

    def level_order_successor(self, root, key):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
            if currentNode.val == key:
                break
        return queue[0] if queue else None

    def connect_lvl_order_siblings(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            prevNode = None
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                # connect node
                if prevNode:
                    prevNode.next = currentNode
                prevNode = currentNode
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return root

    def connect_all_siblings(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            prevNode = None
            levelSize = len(queue)
            currentNode = queue.popleft()
            if prevNode:
                prevNode.next = currentNode
            prevNode = currentNode
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return root

    def right_side_view(self, root):
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                currentNode = queue.popleft()
                if (i == levelSize - 1):
                    result.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                
        return result
            



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(root.print_bfs(root))


