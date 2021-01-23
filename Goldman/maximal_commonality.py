import collections

class Solution:
    def maxCommon(self, s):
        out = 0
        left = collections.Counter('')
        right = collections.Counter(s)
        
        for i,c in enumerate(s):
            left[c] += 1
            right[c] -= 1
            
            out = max(out, sum((left&right).values()))
        
        return out

s = Solution()
print(s.maxCommon('abcdedeara'))