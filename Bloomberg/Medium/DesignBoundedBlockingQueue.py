from collections import deque

# threading is a CPU Bound Task
# There are three ways
# 1. Semaphore - Too Easy

from threading import Lock, Semaphore, Condition


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.e = Semaphore(capacity)
        self.d = Semaphore(0)
        self.q = []

    def enqueue(self, element: int) -> None:
        self.e.acquire()
        self.q.append(element)
        self.d.release()

    def dequeue(self) -> int:
        self.d.acquire()
        element = self.q.pop(0)
        self.e.release()
        return element

    def size(self) -> int:
        return len(self.q)


# 2.  Condition Threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.c = Condition()
        self.q = deque()
        self.cap = capacity

    def enqueue(self, element: int) -> None:
        self.c.acquire()
        while self.size == self.cap:
            self.c.wait()
        self.q.append(element)
        self.c.notifyAll()
        self.c.release()

    def dequeue(self) -> int:
        self.c.acquire()
        while self.size() == 0:
            self.c.wait()
        ans = self.q.popleft()
        self.c.notifyAll()
        self.c.release()
        return ans

    def size(self) -> int:
        return len(self.q)


# 3. Threading Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en = Lock()
        self.de = Lock()
        self.q = deque()
        self.cap = capacity
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if self.size() < self.cap:
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        ans = self.q.popleft()
        if self.size() > 0:
            self.de.release()
        if self.en.locked():
            self.en.release()
        return ans

    def size(self) -> int:
        return len(self.q)


