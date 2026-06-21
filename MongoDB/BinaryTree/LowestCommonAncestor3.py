# Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None

# Clarify: guaranteed both p and q exist in the same tree? small in-memory tree?
# Key insight: this is the SAME pattern as "linked list intersection" —
#              walking up via .parent is just traversing two linked lists toward a shared tail

# ─── Approach 1: Set of Ancestors — O(d1 + d2) time | O(d1) space ───
# Volunteer: simplest to reason about, but uses extra space to store ancestors
class SolutionSet:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = set()

        node = p
        while node:                            # walk p up to the root, recording every ancestor
            ancestors.add(node)
            node = node.parent

        node = q
        while node:                            # walk q up, first match is the LCA
            if node in ancestors:
                return node
            node = node.parent

        return None                            # no common ancestor (shouldn't happen if same tree)


# ─── Approach 2: Two Pointers — O(d1 + d2) time | O(1) space ───
# Volunteer: optimal — no extra data structure, same idea as linked list intersection
# Why flip works: equalizes path lengths so both pointers traverse the same TOTAL distance
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr1, ptr2 = p, q

        while ptr1 != ptr2:
            ptr1 = ptr1.parent if ptr1 else q   # hit top → restart from q's original position
            ptr2 = ptr2.parent if ptr2 else p   # hit top → restart from p's original position

        return ptr1                             # they meet exactly at the LCA

# ─── Decision guide ──────────────────────────────────────────────────
# Want simplicity / readability  → Approach 1 (Set)
# Want O(1) space                → Approach 2 (Two Pointers) — preferred in interview

# Edge cases (both):
#   p == q → Approach 1 finds match immediately; Approach 2 loop never runs
#   p is ancestor of q → both handle correctly
#   p and q same depth → meet without ever needing to flip (Approach 2)

# Complexity:
#   Approach 1 → O(d1 + d2) time | O(d1) space for the set
#   Approach 2 → O(d1 + d2) time | O(1) space

# Follow-ups:
#   No parent pointers, given root instead → use general tree DFS (see LCA of Binary Tree)
#   Why does Approach 2 always terminate? → combined path length equalized after at most 1 flip each
#   N nodes instead of 2 → doesn't generalize as cleanly, would need binary lifting or similar
#   Same pattern elsewhere → linked list intersection, cycle detection (Floyd's algorithm)