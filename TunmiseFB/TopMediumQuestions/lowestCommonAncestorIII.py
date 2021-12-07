#https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

'''
APPROACH 2: 

We can list all the ancestors of each node, and compare the two ancestor lists from the root node down, until we reach the last same element in the two lists. (or until we reach the last element of the list if one node is an ancestor of the other)

'''


def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_list = []
        while p:
            p_list.append(p)
            p = p.parent
        
        q_list = []
        while q:
            q_list.append(q)
            q = q.parent
        
        min_length = min(len(p_list), len(q_list))
        i = 1
        while i <= min_length:
            if q_list[-i] != p_list[-i]:
                return q_list[-i + 1]
            i += 1
        return q_list[-i + 1]




'''

APPROACH 1: ITERATIVE

The idea is to store the parents (path) from root to p, and then check q's path.

'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p:
            path.add(p)
            p = p.parent 
        while q not in path:
            q = q.parent 
        return q


