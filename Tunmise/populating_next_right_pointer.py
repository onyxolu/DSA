class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.connectNodes(root.left,root.right)
        return root
        
    def connectNodes(self,root1,root2):
        if not root1 and not root2:
            return
        root1.next =root2
        root2.next = None
        self.connectNodes(root1.left,root1.right)
        self.connectNodes(root1.right,root2.left)
        self.connectNodes(root2.left,root2.right)