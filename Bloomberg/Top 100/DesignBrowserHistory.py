
# LRU Cache
# Key = url, val = node.
# Bloomberg Version


class Node():
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.totalCount = 0
        self.cache = {}

        # left = least recent  , right = Most recent. See it as head and tail
        self.left, self.right = Node(None), Node(None)
        self.left.next, self.right.prev = self.right, self.left
        self.visit(homepage)

    def insert(self, node):
        # adds to the right
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        # fhjjfjf

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def visit(self, url: str) -> None:
        self.current += 1
        if url in self.cache:
            self.remove(self.cache[url])
            del self.cache[url]
        self.insert(self.cache[url])
        self.cache[url] = Node(url)

    def print(self):
        curNode = self.right.prev
        while curNode.prev:
            print(curNode.url)
            curNode = curNode.prev

    def back(self, steps: int) -> str:
        if len(self.cache) < steps:
            return self.left.next
        else:
            stepsCount = steps
            while stepsCount > 0:
                curNode = self.right.prev
                del self.cache[curNode.url]
                self.remove(self.cache[curNode.url])
                stepsCount -= 1
        return self.right.prev.url


# Key = idx, val = node.
class Node():
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        # Set head and tail
        self.head = Node(homepage)
        self.tail = Node(None)

        # update doubly linked list next and prev pointers
        self.head.next = self.tail
        self.tail.prev = self.head

        # Have a cache to save nodes with indexes
        self.currentIdx = 0
        self.totalCount = 1
        self.history = {0: self.head}

    def addAfter(self, currentNode, newNode):
        currentNode.next = newNode
        newNode.prev = currentNode

        self.tail.prev = newNode
        newNode.next = self.tail

    def visit(self, url: str) -> None:
        # get current node
        currentNode = self.history[self.currentIdx]
        # add to end of LL
        self.addAfter(currentNode, Node(url))
        # update index
        self.currentIdx += 1
        self.totalCount = self.currentIdx + 1
        # add new node to cache
        self.history[self.currentIdx] = currentNode.next

    def back(self, steps: int) -> str:
        # check for steps > currentIdx
        idx = max(0, self.currentIdx - steps)
        self.currentIdx = idx
        return self.history[idx].url

    def forward(self, steps: int) -> str:
        # check for steps > totalcount
        idx = min(self.currentIdx + steps, self.totalCount - 1)
        self.currentIdx = idx
        return self.history[idx].url


# Array

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.current += 1
        self.history = self.history[:self.current]  # keep track of current
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current = max(self.current-steps, 0)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.current+steps, len(self.history)-1)
        return self.history[self.current]
