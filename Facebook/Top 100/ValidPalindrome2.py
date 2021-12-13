# deleting at most one character from it

# Two pointers

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1
        while l < r:
            if s[l] != s[r]:
                #do a check
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            l += 1
            r -= 1
        return True
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            


# Recursive 


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s, one):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                elif one == False:
                    return valid(s[left:right], True) or valid(s[left + 1 : right + 1], True)
                else:
                    return False
            return True
                    
        return valid(s, False)