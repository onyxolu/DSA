

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dict = {}
        for val in s:
            val_lower = val.lower()
            if val_lower in dict:
                dict[val_lower] += 1 
            else:
                dict[val_lower] = 1

        count = 0
        for x in dict.values():
            if x % 2 != 0:
                count += 1

        return count <= 1