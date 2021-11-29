
from collections import deque, List, read4

class Solution:
    def __init__(self):
        self.q = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                buf4 = ['']*4
                v = read4(buf4)
                if v == 0:
                    break
                self.q += buf4[:v]
        return i