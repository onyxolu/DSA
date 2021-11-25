

# Since it is a tree, we have to traverse the tree

#BFS

from collections import defaultdict, deque
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # get parent child relationship
        
        node_dict = defaultdict(list)
        
        for i, pp in enumerate(ppid):
            node_dict[pp].append(pid[i])
        
        # Do BFS
        queue = deque([kill])
        result = []
        while queue:
            parent_node = queue.popleft()
            result.append(parent_node)
            queue.extend(node_dict[parent_node])
        return result




# dfs


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        import collections
        graph = collections.defaultdict(list)
        output = []

        def dfs(curr_node):
            output.append(curr_node)
            children = graph[curr_node]
            for child in children:
                dfs(child)

        for i in range(len(ppid)):
            parent = ppid[i]
            child = pid[i]
            graph[parent].append(child)


        dfs(kill)
        return output
    