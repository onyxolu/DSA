
# Variable
# Vertices - Nodes
# Edges - Lines

# BFS Analysis
# Time Complexity = 0(V+E)
# Space Complexity = 0(V)



class Node: 
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self,array):
        queue = [self]
        while len(queue) > 0:
            current = queue[0]
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
    