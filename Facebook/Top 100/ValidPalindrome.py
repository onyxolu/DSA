
# 0(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for val in s:
            if val.isalnum():
                clean_str += val.lower()
        left = 0
        right = len(clean_str) -1
        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left +=1
            right -= 1
        return True
    