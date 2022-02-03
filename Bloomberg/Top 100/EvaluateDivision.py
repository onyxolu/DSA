
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        
        
        a -> b = 2 ; b -> a = 1/2
        b -> c = 3 ; c -> b = 1/3
        
        a -> c = a -> b * b -> c = 2 * 3
        
        1. build graph
        2. BFS scan all -> get result map
        3. scan queries get result
        
        
        """
        M = defaultdict(dict)
        
        # Build graph
        for e, v in zip(equations, values):
            M[e[0]][e[1]] = v
            M[e[1]][e[0]] = 1 / v
        
        res = {}
        # {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.3333333333333333}})

          
        def BFS(i, t):
            if (i, t) in res:
                return res[(i, t)]
            
            Q = deque([(i, 1)])
            
            while Q:
                n, mul = Q.popleft()
                for e in M[n]:
                    if (i, e) not in res:
                        res[(i, e)] = mul * M[n][e]
                        Q.append((e, res[(i, e)]))
#          deque([('b', 2.0)])
# deque([('a', 1.0), ('c', 6.0)])
# deque([('c', 6.0)])
# deque([])
# deque([('a', 0.5), ('c', 3.0)])
# deque([('c', 3.0), ('b', 1.0)])
# deque([('b', 1.0)])
# deque([])
# deque([])
# deque([])

            if (i,t) not in res:
                res[(i, t)] = -1
            return res[(i, t)]
        
        return [BFS(q[0], q[1]) for q in queries]