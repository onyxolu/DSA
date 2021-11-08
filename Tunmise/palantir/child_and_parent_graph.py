"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, the earliest ancestor of 6 is 14, and the earliest ancestor of 15 is 2. 

         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11

Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return any one of them. If the input individual has no parents, the function should return null (or -1).

Sample input and output:

parent_child_pairs_3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

find_earliest_ancestor(parent_child_pairs_3, 8) => 14
find_earliest_ancestor(parent_child_pairs_3, 7) => 14
find_earliest_ancestor(parent_child_pairs_3, 6) => 14
find_earliest_ancestor(parent_child_pairs_3, 15) => 2
find_earliest_ancestor(parent_child_pairs_3, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_3, 11) => 14


Additional example:

  14
  |
  2      4    1
  |    / | \ /
  3   5  8  9
 / \ / \     \
15  6   7    11

parent_child_pairs_4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]

find_earliest_ancestor(parent_child_pairs_4, 8) => 4
find_earliest_ancestor(parent_child_pairs_4, 7) => 4
find_earliest_ancestor(parent_child_pairs_4, 6) => 14
find_earliest_ancestor(parent_child_pairs_4, 15) => 14
find_earliest_ancestor(parent_child_pairs_4, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_4, 11) => 4 or 1

n: number of pairs in the input


"""



def relationships(pairs):
    import collections
    allNodes = set() # o(a)
    graph = collections.defaultdict(list) #-o(a)
    
    for parent ,child in pairs:     # -> O(n)
        graph[child].append(parent)
        allNodes.add(parent)
        allNodes.add(child)
        
    zeroParents = [] # o(L)
    oneParent = [] # O(h)
    
    for node in allNodes: # -> a = numOfNodesin Graph -> 0(A)
        if graph[node] == []:
            zeroParents.append(node)
            
        elif len(graph[node]) ==1:
            oneParent.append(node)
        
    return zeroParents, oneParent


parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2), 
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]


parent_child_pairs_3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

parent_child_pairs_4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]


#print(relationships(parent_child_pairs))


def ancestorExists(pairs, p,q):
    import collections
    allNodes = set() # o(a)
    graph = collections.defaultdict(list) #-o(a)
    
    for parent ,child in pairs:     # -> O(n)
        graph[child].append(parent)
        allNodes.add(parent)
        allNodes.add(child)
        
    
    def path(node):
        pathSoFar = []
        def dfs(node):
            pathSoFar.append(node)
            edges = graph[node]
            for edge in edges:
                dfs(edge)
                
        dfs(node)  
        return pathSoFar

    resultP = path(p) 
    resultQ = path(q) 
    
    setQ = set(resultQ)
#     print(resultP)
#     print(resultQ)
    
    for node in resultP:
        if node in setQ and node != resultP[0] and node != resultQ[0]:
            return True
        
    return False



def farthest(pairs, p):
    import collections
    allNodes = set() # o(a)
    graph = collections.defaultdict(list) #-o(a)
    
    for parent ,child in pairs:     # -> O(n)
        graph[child].append(parent)
        allNodes.add(parent)
        allNodes.add(child)
        
    def path(node):
        pathSoFar = []
        def dfs(node):
            pathSoFar.append(node)
            edges = graph[node]
            for edge in edges:
                dfs(edge)
                
        dfs(node)  
        return pathSoFar

    resultP = path(p)
    print(resultP)
    return resultP[-1] if resultP [-1] != p else -1
 

# print(farthest(parent_child_pairs_4,8))
# print(farthest(parent_child_pairs_4,7))
print(farthest(parent_child_pairs_4,6))
print(farthest(parent_child_pairs_4,15))
print(farthest(parent_child_pairs_4,14)) # None
print(farthest(parent_child_pairs_4,11))

# find_earliest_ancestor(parent_child_pairs_4, 8) => 4
# find_earliest_ancestor(parent_child_pairs_4, 7) => 4
# find_earliest_ancestor(parent_child_pairs_4, 6) => 14
# find_earliest_ancestor(parent_child_pairs_4, 15) => 14
# find_earliest_ancestor(parent_child_pairs_4, 14) #null , -1
# find_earliest_ancestor(parent_child_pairs_4, 11) => 4 or 1