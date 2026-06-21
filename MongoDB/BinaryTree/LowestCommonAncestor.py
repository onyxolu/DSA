from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Clarify: can p or q be the root? guaranteed both exist in the tree? small in-memory tree?
# Key insight: at each node, check 3 things — left subtree has target, right subtree has target,
#              current node IS a target. If any 2 of 3 are true → this node is the LCA.

# ─── Approach 1: General Binary Tree — O(n) time | O(h) space ───
# Volunteer: function returns the actual LCA node directly, no instance variable needed
# Base case root==p or root==q handles "current node is a target" implicitly
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root                        # found a target, or hit the bottom

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:                     # found one on each side → current is LCA
            return root
        return left or right                   # propagate whichever side found something


# ─── Approach 2: Binary Search Tree — O(log n) time | O(1) space (iterative) ───
# Volunteer: BST property means we don't need to search both subtrees
# If both p,q < node → LCA is in left subtree. If both > node → LCA is in right subtree.
# Otherwise → node is the split point → node is the LCA
class SolutionBST:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left               # both smaller → go left
            elif p.val > node.val and q.val > node.val:
                node = node.right              # both larger → go right
            else:
                return node                    # split point found → this is the LCA
        return None

# Edge cases:
#   p or q is the root → root is immediately the LCA
#   p is an ancestor of q → base case catches p, propagates up through right=None
#   p and q in different subtrees → left and right both truthy at their common ancestor

# Complexity:
#   General tree → O(n) time, O(h) space (recursion stack)
#   BST          → O(log n) time average, O(1) space (iterative, no recursion needed)
#   BST worst case → O(n) time if tree is skewed (unbalanced)

# Follow-ups:
#   Tree has parent pointers instead of root access → see LCA III, different approach entirely
#   N nodes instead of 2 → same pattern, track count of targets found in each subtree
#   What if p or q doesn't exist in tree? → add existence check first, or return None safely
#   Why is BST faster? → sorted property lets you discard half the tree at each step, like binary search