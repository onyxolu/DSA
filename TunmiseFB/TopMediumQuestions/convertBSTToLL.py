'''

We can traverse using BFS or DFS.

Algorithm

Standard inorder recursion follows left -> node -> right order, where left and right parts are the recursion calls and node part is where all processing is done.

Processing here is basically to link the previous node with the current one, and because of that one has to track the last node which is the largest node in a new doubly linked list so far.

One more detail : one has to keep the first, or the smallest, node as well to close the ring of doubly linked list.

Here is the algorithm :

1. Initiate the first and the last nodes as nulls.

2. Call the standard inorder recursion helper(root) :

    If node is not null :

        Call the recursion for the left subtree helper(node.left).

        If the last node is not null, link the last and the current node nodes.

        Else initiate the first node.

        Mark the current node as the last one : last = node.

        Call the recursion for the right subtree helper(node.right).

3. Link the first and the last nodes to close DLL ring and then return the first node.

Time complexity - O(N) since each node is processed exactly once.

Space complexity - O(N). We have to keep a recursion stack of the O(N) for the worst case of completely unbalanced tree.

'''


class Solution(object):
    head = None
    prev = None

    def treeToDoublyList(self, root):
        if not root: return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node: return
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:  # We are at the head.
            self.head = node
        self.prev = node
        self.treeToDoublyListHelper(node.right)




'''
MORRIS TRAVERSAL WITH O(1) SPACE 

Morris traversal should be O(1) extra space. You cant count the solution set as extra space since that was what was asked in the first place.
The whole point of Morris traversal is to eliminate the need for extra space(either call stack or stack in interative method).
No point of doing all that extra work of modifying all the nodes for no gain in time or space complexity.


Pseudo Code
1. Initialize current as root 
2. While current is not NULL
   If current hs a left child
      ifa) Make current as right child of the rightmost 
         node in current's left subtree
      ifb) Go to this left child, i.e., current = current->left
   Else
      ea) Print current’s data
      eb) Go to the right, i.e., current = current->right

'''

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        first, prev = None, None
        
        while root:
            if root.left:
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                
                if pred.right: # already visited root's predecessor, now visit root (keep pred pointer to root)
                    root.left = prev
                    prev = root
                    root = root.right  # no more nodes to visit towards the left, so time to go right
                else:
					# have not seen root's predecessor before. Create pointer from pred to root so we can visit root again later
                    pred.right = root
                    root = root.left  # still unvisited nodes in the left subtree, go to the left
                    
            else:
                # there's nothing else before this root that hasn't been visited, visit it
                if prev:
                    root.left = prev
                    prev.right = root
                else:
					# if this is the first node, set it to first
                    first = root
                prev = root  # update prev
                root = root.right
        
        first.left = prev
        prev.right = first
        return first