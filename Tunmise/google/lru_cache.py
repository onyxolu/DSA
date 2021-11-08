class LinkedListNode:
    
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity

        self._lru_cache = self._head_node = LinkedListNode()
        self._tail_node = LinkedListNode()
        
        self._head_node.next = self._tail_node
        self._tail_node.prev = self._head_node
    
        self.existing_nodes = {}
    
    def _add_to_head(self,node):
        
        self._head_node.next, node.next = node, self._head_node.next
        node.prev, node.next.prev = self._head_node, node
        
        self.existing_nodes[node.key] = node
        
        if len(self.existing_nodes) > self.capacity:
            self._remove_from_tail()
        
        return
    
    def _remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return
        
    def _remove_from_tail(self):
        node = self._tail_node.prev
        self._remove_node(node)
        del self.existing_nodes[node.key]
        return
        
    def get(self, key: int) -> int:
        
        if key not in self.existing_nodes:
            return -1
        else:
            node = self.existing_nodes[key]
            self._remove_node(node)
            self._add_to_head(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.existing_nodes:
            node = LinkedListNode(key, value)
        else:
            node = self.existing_nodes[key]
            node.val = value
            self._remove_node(node)
        
        self._add_to_head(node)
        return