class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, v in enumerate(s):
            n = s.count(v)
            if n == 1:
                return i
            else:
                continue
        return -1
                
            