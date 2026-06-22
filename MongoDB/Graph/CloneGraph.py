from typing import Optional

# Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# Clarify: undirected (mutual connections)? neighbor order matters? graph could have cycles?
# Key insight: graph has cycles → need a hashmap to avoid infinite recursion
#              must store clone in hashmap BEFORE recursing into neighbors

# ─── Approach 1: Brute Force (Two-Pass) — O(n + e) time | O(n) space ───
# Volunteer: first pass creates all node copies, second pass wires up neighbors
# Less efficient than single-pass DFS, but easier to reason about initially
class SolutionBruteForce:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        # First pass: BFS/DFS to discover all nodes, create copies (no neighbors yet)
        visited = set()
        stack = [node]
        visited.add(node)
        oldToNew[node] = Node(node.val)

        while stack:
            cur = stack.pop()
            for nei in cur.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    oldToNew[nei] = Node(nei.val)
                    stack.append(nei)

        # Second pass: wire up neighbors using the map
        for old_node, new_node in oldToNew.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(oldToNew[nei])

        return oldToNew[node]


# ─── Approach 2: Single-Pass DFS — O(n + e) time | O(n) space ───
# Volunteer: store clone in map BEFORE recursing → breaks cycles automatically
# Real world: serializing/deserializing object graphs, deep copying linked structures with cycles
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]              # already cloned — breaks the cycle

            copy = Node(node.val)
            oldToNew[node] = copy                  # store BEFORE recursing — critical step

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None

# ─── Decision guide ──────────────────────────────────────────────────
# Both same complexity → single-pass DFS preferred for cleaner code, one less map iteration

# Edge cases:
#   node is None → return None
#   single node, no neighbors → returns clone with empty neighbor list
#   cycle (1↔2) → hashmap check prevents infinite recursion

# Complexity:
#   time  → O(n + e) where n = nodes, e = edges
#   space → O(n) for hashmap + O(n) recursion stack worst case (line graph)

# Follow-ups:
#   Why store in map before recursing, not after? → after would cause infinite recursion on cycles
#   BFS instead of DFS? → same complexity, use a queue instead of recursion, avoids stack overflow on deep graphs
#   What if graph is disconnected? → wouldn't apply here, problem guarantees connected graph
#   Very large graph → BFS iterative version avoids recursion depth limits