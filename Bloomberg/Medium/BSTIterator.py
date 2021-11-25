
# Inorder Traversal

class BSTIterator:
  def dfs(self, node):
    if node.left:
      yield from self.dfs(node.left)
    
    yield node.val
    
    if node.right:
      yield from self.dfs(node.right)
    

  def __init__(self, root):
    self.gen = self.dfs(root)
    self.peek = next(self.gen)

  def next(self) -> int:
    next_node, self.peek = self.peek, None
    try:
      self.peek = next(self.gen)
    except:
      self.peek = None
    return next_node

  def hasNext(self) -> bool:
    return self.peek is not None


# Stack

from collections import deque


class BSTIterator:
    def __init__(self, root):
        self._tree_stack = deque()
        self._tree_stack.append(root)
        self._extend_stack_to_left()
    
    def _extend_stack_to_left(self):
        while self._tree_stack[-1].left is not None:
            self._tree_stack.append(self._tree_stack[-1].left)

    def next(self) -> int:
        node = self._tree_stack.pop()
        if node.right is not None:
            self._tree_stack.append(node.right)
            self._extend_stack_to_left()
        return node.val 

    def hasNext(self) -> bool:
        return len(self._tree_stack) > 0