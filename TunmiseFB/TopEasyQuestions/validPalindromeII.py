'''
OPTIMAL
We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. 
Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. 
We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.

We only compare substring from left to right pointer and left+1 to right+1

We form two sub strings, one including the left and excluding the right and one excluding the 
left and including the right.

e.g - abaaaaaca

Time: O(n) - The left-right movement inward is O(N), and the mismatch check which happens a maximum of one time is also O(N).
Space: O(n) - worst case is the first and last index are different, now we have to form substring containing all of them
'''

class Solution(object):
    def validPalindrome(s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left = left + 1
            right = right - 1
        return True










'''
Recursive solution, which is very slow compared to the other one, when we encounter different values,
we basically move forward by one and compare if they will be the same, and then increment count by one, 
once count is greater than 1, we exit the recursion.

Time complexity - 
'''

def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    count = 0
                
    def isPalindrome(l, r, count):
        if count > 1:
            return False
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            if s[l] != s[r]:
                if s[l+1] != s[r] and s[l] != s[r-1]:
                    return False
                return isPalindrome(l+1, r, count+1) or isPalindrome(l, r-1, count+1)
                
        return True
    
    return isPalindrome(l, r, count)