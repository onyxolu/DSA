
# Steps
# brute force - bin to int, add the int, int to bin
# We use the normal maths method to add binary
# we reverse the bin strings to simulate calc from the back
# Edge case 1+1+1, this will handle it, total = digitA + digitB + carry
# We use carry var to simulate carry in the  calc
# we add the extra carry 1 in the end

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Brute force - bin to int, add, int to bin
        # valSum = int(a, 2) + int(b, 2)
        # ans = "{0:b}".format(valSum)
        # return ans
        #   1 1
        # +   1
        # ------
        # 1 0 0
        # ------
        
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            
            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
            
        if carry: # extra carry 1 at the end
            res = "1" + res
            
        return res