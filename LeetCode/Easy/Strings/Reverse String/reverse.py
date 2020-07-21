class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, val in enumerate(s[::-1]):
            s[i] = val 