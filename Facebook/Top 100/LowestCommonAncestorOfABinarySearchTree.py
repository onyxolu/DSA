
from collections import Node

# Optimal - OPTIMALLLLLLLLLLLLLLLLLLLLLLLLLL

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
          
        # nodep and nodeq to save the ancestor nodes
        # O(n) time O(1) space
        nodeP,nodeQ=p,q
        while p!=q:
            p=p.parent if p.parent else nodeQ
            q=q.parent if q.parent else nodeP
        
        return p


# set

# TC - 0(N) SC- 0(N)


def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        lookup = set()
        # Traverse up the tree till root and keep storing node values in a Set
        while (p != None):
            lookup.add(p.val)
            p = p.parent
        
        # Find the common value between q node and set and that is the LCA
        while(q != None):
            if q.val in lookup:
                return q
            q = q.parent