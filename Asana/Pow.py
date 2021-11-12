
# Recursion
# Time => 0(LogN)
# Space => 0(logN)

def Pow(x,n):
    def helper(x,n):
        # Base Case
        if x == 0: return 0
        if n == 0: return 1
        if x == 1: return 1

        # x * x^2 * x^2 = x^5
        res = helper(x, n//2)
        res *= res
        return x * res if x %2 != 0 else res

    res = helper(x,abs(n))
    return res if n >= 0 else 1/res