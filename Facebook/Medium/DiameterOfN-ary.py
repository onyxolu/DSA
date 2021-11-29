

# left rotation on an array


class Solution:
    def diameter(self, root) -> int:
        def dfs(node):
            if not node.children: return [0, 0]
            
            maxD, vals = 0, [0,  0]
            for child in node.children:
                maxDSubtree, depth = dfs(child)
                maxD = max(maxD, maxDSubtree)
                
                depth = depth + 1
                
                if depth > vals[0]:
                    vals[1] = vals[0]
                    vals[0] = depth
                else:
                    vals[1] = max(vals[1], depth)
        
            maxD = max(maxD, sum(vals))
            return [maxD, vals[0]]
        
        maxD, _ = dfs(root)
        return maxD








