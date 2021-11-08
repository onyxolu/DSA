from typing import Collection, List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Collection.defaultdict(list)

        for idx in range(len(equations)):
            numerator = equations[idx][0]
            denominator = equations[idx][1]
            graph[numerator].append([denominator, values[idx]])
            graph[denominator].append([numerator, 1/values[idx]])

        def dfs(numerator, multiplier, denominator):
            ans = None
            for denom, val in graph[numerator]:
                if denom not in seen:
                    seen.add(denom)
                    if denom == denominator:
                        return multiplier * val
                    else:
                        ans = dfs(denom, multiplier * val, denominator)
                        if ans is not None:
                            return ans
            return ans
 
        calculations = []
        for query in queries:
            numerator = query[0]
            denominator = query[1]
            seen = set()
            ans = dfs(numerator, 1, denominator)
            if ans is not None:
                calculations.append(ans)
            else:
                calculations.append(-1.0)

        return calculations

#solution 2
import collections
class Solution(object):
    def evalQuery(self, op1, op2):
        
        if not op1 in self.variables or not op2 in self.variables:
            return -1
        
        if op1 == op2:
            return 1
        
        bfsq = [(op1,1)]
        val = 0
        vis = set()
        
        while bfsq:
            
            cur, val = bfsq.pop(0)
            vis.add(cur)
            
            if cur == op2:
                return val
            
            for neigh in self.graph[cur]:
                if not neigh in vis:
                    bfsq.append((neigh, val*self.graph[cur][neigh]))
        
        return -1
            
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        self.graph = collections.defaultdict(dict)
        
        self.variables = set()
        
        for index, equ in enumerate(equations):
            self.graph[equ[0]][equ[1]] = values[index]
            self.graph[equ[1]][equ[0]] = 1/values[index]
            self.variables.add(equ[0])
            self.variables.add(equ[1])
        
        res = []
        
        for query in queries:
            res.append(self.evalQuery(query[0], query[1]))
            
        return res
          