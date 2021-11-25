

class Solution:
    
    # Top Down + Memoization
    # Time : O(n)
    # Space: O(n)
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        @lru_cache(maxsize=len(s))
        def decodingsFromHere(i):
            
            if i >= n:
                return 1
             
            if s[i] == '0':
                return 0
            
            count = decodingsFromHere(i + 1)
            
            if i < n - 1 and int(s[i:i+2]) <= 26:
                count += decodingsFromHere(i + 2)
            
            return count
        
        return decodingsFromHere(0)
    
    
    # Bottom Up Dynamic Programming
    # Time : O(n)
    # Space: O(1)
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        prev = 1
        prevPrev = 1
        
        for i in range(n - 1, -1, -1):
            newCount = 0
            
            if s[i] != '0':
                newCount += prev

                if i < n - 1 and int(s[i:i+2]) <= 26:
                    newCount += prevPrev              
            
            prev, prevPrev = newCount, prev
            
        return prev
        