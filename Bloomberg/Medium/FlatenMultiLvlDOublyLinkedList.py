
# We  can do recursion but stack is intuitive

# 1--2--3--4--5--6
#       7--8--9--10
#          11--12--null

# [3,4(next),7(child)]
# 1 => 2 => 3 => 7 => 8

# Next first, then child of next

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        dummy = Node(0)
        cur, stack = dummy , [head]
        while stack:
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)
            cur.next = tmp # Structure dummy we are returning
            tmp.prev = cur # set the previous for the dummy
            tmp.child = None # remove childs
            cur = tmp  # Move pointer head
        dummy.next.prev = None 
        return dummy.next



# Recursion

def flatten(self, head: 'Node') -> 'Node':
    def getTail(node):
        prev = None
        while node:
            _next = node.next
            if node.child:
                # ... <-> node <-> node.child <-> ...
                node.next = node.child
                node.child = None
                node.next.prev = node
                # get the end node of the node.child list
                prev = getTail(node.next)
                if _next:
                    # ... <-> prev (end node) <-> _next (originally node.next) <-> ...
                    _next.prev = prev
                    prev.next = _next
            else:
                prev = node
            node = _next  # loop through the list of nodes
        return prev  # return end node
    
    getTail(head)
    return head