

class Solution:
    def postorder_left(self, root, result):
        if root:
            result.append(root.val)
            self.postorder_left(root.left, result)
            self.postorder_left(root.right, result)
        else:
            result.append('null')
    
    def postorder_right(self, root, result):
        if root:
            result.append(root.val)
            self.postorder_right(root.right, result)
            self.postorder_right(root.left, result)
        else:
            result.append('null')
    
        
    def isSymmetric(self, root):
        if root:
            left = []
            right = []
            self.postorder_left(root.left, left)
            self.postorder_right(root.right, right)
            print(left, right)
            if left == right: return True
            else: return False
        else: return True

