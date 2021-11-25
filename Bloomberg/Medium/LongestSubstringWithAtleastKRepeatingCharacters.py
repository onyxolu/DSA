

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # say we have "aaabbeeeefff" and k is 3 we break it when we see b so we have "aaa" and "eeeefff" , we can see we have sub problems, so, recursive
        # Time = 0(N + N)
        # Space = 0(26) Map, constant
        
        n = len(s)
        if n == 0 or n < k: return 0
        if k <= 1: return n

        counts = Counter(s)

        l = 0
        while l < n and counts[s[l]] >= k: l += 1 # "aaabbeeeefff" => "aaa"
        if l >= n-1: return l

        ls1 = self.longestSubstring(s[0:l], k)
        while l < n and counts[s[l]] < k: l += 1 # "aaabbeeeefff" => "eeeeff"
        ls2 = self.longestSubstring(s[l:], k) if l<n else 0
        return max(ls1, ls2)
        

        
        