'''
Approach 1: Using DFS

We traverse the tree using a depth first search. If node.val falls outside the range, (for example node.val < L), then we know that only the right branch could have nodes with value inside [L, R].

Time Complexity: O(N), where NN is the number of nodes in the tree.

Space Complexity: O(N)

For the recursive implementation, the recursion will consume additional space in the function call stack. In the worst case, the tree is of chain shape, and we will reach all the way down to the leaf node.

For the iterative implementation, essentially we are doing a BFS (Breadth-First Search) traversal, where the stack will contain no more than two levels of the nodes. The maximal number of nodes in a binary tree is N/2. Therefore, the maximal space needed for the stack would be O(N).
'''


class Solution(object):
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        else:
            total = 0
            if low <= root.val <= high:
                total += root.val
            if root.val > low:
                total += self.rangeSumBST(root.left, low, high)
            if root.val < high:
                total += self.rangeSumBST(root.right, low, high)
            return total    


# recursive approach

class Solution(object):
    def rangeSumBST(self, root, low, high):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans




'''
Approach 2: Using BFS

Starting from the root node, we check if the current node is within range, if it is, we increment our sum else if its appedn the left and right node to our queue, we check if the left is > low and right is les than hihg, cos its a tree, so its sorted, left and right.
'''

from collections import deque

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        
        sum = 0
        if not root:
            return sum
        q = deque([root])
        while q:
            curNode = q.popleft()
            if curNode.val >= low and curNode.val <= high:
                sum += curNode.val
            if curNode.left and curNode.val > low:
                q.append(curNode.left)
            if curNode.right and curNode.val < high:
                q.append(curNode.right)
                
        return sum