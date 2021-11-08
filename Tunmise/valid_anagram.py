class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        #table = [0] * 128
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                d[i] = 1
        for i in d.values():
            if i > 0:
                return False
        return True