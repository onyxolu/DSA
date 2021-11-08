from collections import defaultdict
def vertical_level_order_traversal(root):
    if not root:
        return
    d = defaultdict(list)
    dfs(root,0,d)
    
    l =sorted(d.items(),key = lambda x:x[0])
    for i,val in enumerate(l):
        l[i]=val
    return l


def dfs(root,index,d):
    if not root:
        return
    d[index].append(root.value)
    dfs(root.left,index-1,d)
    dfs(root.right,index+1,d)

