
from collections import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force
        # 0(n)2*m try every single prefix and check if it's in dictionary
        # e.g l+ allcombo, e+ all combo, c + all combo
        # approach two - check every words in worddict and try to find it in s via sliding window
        # Decision Tree
        # start at i, find the first wordDict, then continue from the last index, e.g "leetcode", find leet and continue from index 4
        # we will have decisions based on the no of words in dict
        # we find find the wordDict that matches first prefix (leet), then we move pointer and find worddict for the next prefix (code)
        # we return true when we reach the end of s
        # we need a cache
        # so for example "catsandog", ["cats","dog","sand","and","cat"] index 7 for "og" is false so dp[7] = false, so when we try dp[7] again, we just return false immediately
        # base case is dp[8] = True for "leetcode", cos if we ever get to the last index then weve found the ans
        # we do bottom up approach from last index, e, de, ode etc and check if it matches any of the words
        # dp[8] = True, dp[7]=dp[6]=dp[5] = False, dp[4] = True, dp[3]=dp[2]=dp[1] = false, dp[0]= True
        # so since we matched the first xter "neet", were we able to match the remainder? "code"
        # dp[0] = dp[0+4] = True return True
        
        # create cache - 1d array
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        # in reverse, we want to try every word in dict
        for i in range(len(s)-1, -1, -1 ):
            for w in wordDict:
                # check if there are enough xters in s to compare
                if (i+len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)] # it will eventually link to dp[len(s)] which is true and dp[0] will be true
                if dp[i]: # if we find a way to word break it
                    break
        return dp[0]
            
        
        