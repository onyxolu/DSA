# def bfs(graph, start, end):
#     queue = []
#     queue.append([start])
    
#     while queue:
        
#         path = queue.pop(0)
#         # print(path)
#         node = path[-1]
        
#         if node == end:
#             print(path)
#         if node in graph:
#             for adj in graph[node]:
#                 new_path = list(path)
#                 new_path.append(adj)
#                 queue.append(new_path)
            
            
def bfsLocalVisited(graph, start, end):
    queue = []
    queue.append(([start], set({start})))
    
    while queue:
        
        path, local_set = queue.pop(0)
        #print(path, local_set)
        
        node = path[-1]
        
        if node == end:
            print(path)
            
        if node in graph:
            for adj in graph[node]:
                if adj not in local_set:
                    new_local = set(local_set)
                    new_path = list(path)
                    
                    new_local.add(adj)
                    new_path.append(adj)
                    
                    queue.append(( new_path, new_local))
               
               
def bfsGlobalVisited(graph, start, end):
    queue = []
    visited = set()
    visited.add(start)
    queue.append([start])
    
    while queue:
        
        path = queue.pop(0)
        # print(path)
        node = path[-1]
        
        if node == end:
            print(path)
        if node in graph:
            for adj in graph[node]:
                if adj not in visited:
                    new_path = list(path)
                    new_path.append(adj)
                    visited.add(adj)
                    queue.append(new_path)
                    
def dfsVisited(graph,start,end):
    path = [start]
    visited =set()
    visited.add(start)

    dfsUtil(start,end,graph,path,visited)

def dfsUtil(source,dest,graph,path,visited):
    if path[-1] == dest:
        print(path)
        return
    if source in graph:
        for edge in graph[source]:
            if edge not in visited:
                path.append(edge)
                visited.add(edge)
                dfsUtil(edge,dest,graph,path,visited)
                path.pop()
                visited.remove(edge)

# #Handles cycles as well using visited set()
# def fetchPaths(self,graph, source, destination):

#     visited = set()
#     visited.add(source)

#     path_so_far = [source]

#     self.fetchPathsUtil(source, destination,graph, path_so_far, visited)

# def fetchPathsUtil(self, source, destination, path_so_far, visited):

#     if path_so_far[-1] == destination:
#         print("->".join(path_so_far))
#         return

#     for city in self.flights[source]:
#         if city not in visited:
#             path_so_far.append(city)
#             visited.add(city)
#             self.fetchPathsUtil(city, destination, path_so_far, visited)

#             visited.remove(city)
#             path_so_far.pop(-1)

graph = {
    "a" : ["b", "c"],
    "b" : ["c", "g"],
    "c" : ["d", "e"],
    "d" : ["h", "f"],
    "e" : ["f"],
    "g" : ["f"],
}

graph2 = {
    "a" : ["b"],
    "b" : ["c"],
    "c" : ["d"],
    "d" : ["a"],
}

# print(bfs(graph2, "a", "f"))

print(bfs1(graph, "a", "f"))

print(bfs2(graph, "a", "f"))

print(dfs(graph, "a", "f"))