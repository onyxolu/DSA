

# Sliding Window - 0(26*n)


def characterReplacement(self, s: str, k: int) -> int:
    
    # brute force => check every substring 0(n)^2 use hashmap
    count = {}
    res = 0
    l = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        
        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l+1)
    return res


# Time = 0(N)

def characterReplacement(self, s: str, k: int) -> int:
    
    # brute force => check every substring 0(n)^2 use hashmap
    count = {}
    res = 0
    l = 0
    maxf = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        
        while (r-l+1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l+1)
    return res

    



    