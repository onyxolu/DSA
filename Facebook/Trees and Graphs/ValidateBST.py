# Time Complexity => 0(N)
# Space => 0(N)

class Solution:
    def isValidBST(self, root) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self,root,min_val,max_val):
        if root == None:
            return True
        elif root.val <= min_val or max_val <= root.val:
            return False
        else:
            return self.helper(root.left,min_val,root.val) and self.helper(root.right,root.val,max_val)
        