"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        maxi = [0] #we need this variable to exist in all of our recursive calls,so we can update it with the longest sequence that we found.
        self.findLongestConsecutiveSequence(root,0,0,maxi)
        return maxi[0]

    def findLongestConsecutiveSequence(self,root,count,target,maxi):
        if not root:
            return
        elif root.val == target:
            count += 1
        else:
            count = 1

        maxi[0] = max(maxi[0],count)
        self.findLongestConsecutiveSequence(root.right,count,root.val + 1,maxi)
        self.findLongestConsecutiveSequence(root.left,count,root.val + 1,maxi)