from typing import Optional

# Clarify: what to return if key doesn't exist? capacity always positive?
# Both get and put must be O(1) → hashmap + doubly linked list
#
# Key insight:
#   hashmap alone → O(1) lookup but no ordering
#   queue alone → O(1) ordering but O(n) delete from middle
#   hashmap + DLL → O(1) lookup AND O(1) delete/insert anywhere
#
# Volunteer before being asked:
#   - Dummy HEAD/TAIL nodes → no null pointer edge cases
#   - LRU = head.next, MRU = tail.prev
#   - get → remove + reinsert at MRU position
#   - put → insert at MRU, evict LRU if over capacity
#   - Real world: browser history, DB buffer pool, CDN edge cache

class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                                    # key → node

        self.head, self.tail = Node(0, 0), Node(0, 0)    # dummy LRU, MRU
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node) -> None:                 # O(1) pointer update
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: Node) -> None:                 # O(1) insert at MRU
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])                  # mark as recently used
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])                  # remove stale node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])                      # insert at MRU

        if len(self.cache) > self.cap:                    # over capacity
            lru = self.head.next                          # evict least recently used
            self.remove(lru)
            del self.cache[lru.key]

# Edge cases:
#   get on empty cache → -1
#   put existing key → update value, move to MRU
#   capacity of 1 → every put evicts previous

# Complexity:
#   get → O(1) time
#   put → O(1) time
#   space → O(capacity)

# Follow-ups:
#   Thread safe version → wrap get/put with threading.Lock
#   Distributed LRU → consistent hashing + per-shard LRU (Redis pattern)
#   TTL eviction → add timestamp to node, background thread to evict expired