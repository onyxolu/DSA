def find(graph,val):
    count = 0
    while val in graph  and val != graph[val]:
        val = graph[val]
        count += 1
    return (val,count)
def degree(relationship):
    graph = {}
    d_order = {}
    d_count = {}
    for parent,child in relationships:
        d_count[child] += 1
        if parent not in d_count:
            d_count[parent] = 0
        
        first = find(graph,parent)
        second = find(graph,child)
        if first[0] != second[0]:
            graph[second[0]] = first[0]

    for key,val in d_count:
        if val == 0 or val == 1:
            res.append(key)
    
    
    
