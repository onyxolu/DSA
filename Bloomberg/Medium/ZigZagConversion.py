
# Time 0(N)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]  # Will work for first and last row
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):# Middle rows (rows decrease twice) also check out of bound
                    res += s[i + increment - 2 * r]
                    
        return res
        