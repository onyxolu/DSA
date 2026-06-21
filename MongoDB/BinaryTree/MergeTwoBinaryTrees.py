from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Clarify: can either tree be null? expected scale (small in-memory)? can we modify input?
# Bottom-up DFS — but value update happens top-down, structure wiring happens bottom-up

# ─── Approach 1: In-Place — O(min(n1,n2)) time | O(1) extra space ───
# Volunteer: modifies t1 directly, no new nodes created — most space efficient
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


# ─── Approach 2: New Tree — O(min(n1,n2)) time | O(min(n1,n2)) space ───
# Volunteer: use when input trees must stay unmodified (e.g. caller still needs originals)
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0               # default to 0 when one side is missing
        v2 = t2.val if t2 else 0
        merged = TreeNode(v1 + v2)             # always create a new node

        merged.left = self.mergeTrees(
            t1.left if t1 else None,
            t2.left if t2 else None
        )
        merged.right = self.mergeTrees(
            t1.right if t1 else None,
            t2.right if t2 else None
        )

        return merged

# ─── Decision guide ──────────────────────────────────────────────────
# Can modify input        → Approach 1 (in-place, O(1) extra space)
# Must preserve input      → Approach 2 (new tree, O(n) space)

# Edge cases (both):
#   both null → None
#   one tree null → Approach 1 returns other unchanged; Approach 2 creates new nodes matching it

# Complexity:
#   Approach 1 → O(min(n1,n2)) time | O(1) extra space (O(h) recursion stack)
#   Approach 2 → O(min(n1,n2)) time | O(min(n1,n2)) space for new nodes