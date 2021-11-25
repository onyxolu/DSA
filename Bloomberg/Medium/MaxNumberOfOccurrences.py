
# Time= 0(nm)  m - max-mn
# Space = 0(nm) 


# no of unique xters less than maxLetter
# len(substr) btw minSize and maxSize
import collections

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)
        n = len(s)
        
        for i in range(n):
            for j in range(i + minSize - 1, min(i + maxSize, n)):
                substr = s[i:j+1] # Condition 2
                if len(set(substr)) <= maxLetters: # condition 1
                    freq[substr] += 1
                
        return max(freq.values(), default = 0)


# Optimize

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)
        n = len(s)
        maxOcc = 0
        
        for i in range(n):
            for j in range(i + minSize - 1, min(i + maxSize, n)):
                substr = s[i:j+1] # Condition 2
                if len(set(substr)) <= maxLetters:
                    freq[substr] += 1
                    maxOcc = max(freq[substr], maxOcc) 
                
        return maxOcc


# Optimal 0(N)

# We find a substr of size x > minSize that is valid
#           unique Characters(x) <= maxLetters
# 
# that a substr of y of x with length = minSize is also valid
#          unique Characters(y) <= maxLetters

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = collections.defaultdict(int)
        n = len(s)
        maxOcc = 0
        
        for i in range(n - minSize + 1):
            substr = s[i:i + minSize] # Condition 2
            print(substr)
            if len(set(substr)) <= maxLetters: # Condition 1
                freq[substr] += 1
                maxOcc = max(freq[substr], maxOcc) 
                
        return maxOcc
        