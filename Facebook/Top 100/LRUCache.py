# Ordered Dict in Python will do it 
# Hashmap + Doubly Linked List

class DoublyLinkedListNode:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev, self.next = None, None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev, self.next = None, None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head, self.tail = None, None

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

class LRUCache:
    def __init__(self, capacity) -> None:
        self.cache = {}
        self.maxSize = capacity or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # optional
        self.updateMostRecent(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLast()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.cache[key].val = value
        self.updateMostRecent(self.cache[key])

    def evictLast(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    