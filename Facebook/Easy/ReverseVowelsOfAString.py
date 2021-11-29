
# Two Pointers

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {
            "a": 1,
            "e": 1,
            "i": 1,
            "o": 1,
            "u": 1
        }
        
        left , right = 0, len(s)-1
        while left < right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[right].lower() in vowels:
                left += 1
            elif s[left].lower() in vowels:
                right -= 1
            else:
                left += 1
                right -= 1
            
        return "".join(s)
            
                