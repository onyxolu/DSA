
# Time = 0(n)^2
# Space = 0(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        currentLongest = [0,1]
        def check_palindrome(s, leftIdx, rightIdx):
            while leftIdx >= 0 and rightIdx < len(s):
                if s[leftIdx] != s[rightIdx]:
                    break

                leftIdx -= 1
                rightIdx += 1
            # print(s[leftIdx + 1: rightIdx], leftIdx, rightIdx)
            strLength = rightIdx - (leftIdx+1)
            return [leftIdx+1, rightIdx]
        
        
        for i in range(len(s)):
            even = check_palindrome(s, i-1, i+1)
            odd = check_palindrome(s, i-1, i)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
            
        return s[currentLongest[0]: currentLongest[1]]
                   