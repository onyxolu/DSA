
# Variable
# Vertices - Nodes
# Edges - Lines

# DFS Analysis
# Time Complexity = 0(V+E)
# Space Complexity = 0(V)



class Node: 
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    