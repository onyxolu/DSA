class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if(x < 0):
            x = -x
            isNeg = True
        x = str(x)
        x = x[::-1]
        x = int(x)
        if not((x <= 2**31 - 1) and (x >= -2**31)):
            return 0
        if isNeg:
            x = -x
        return x
    