
# Recursion
# Time => 0(LogN)
# Space => 0(logN)


# (x)^-1 = 1/x
# (x)^0 = 1
# (0)^x = 0
# (1)^x = 1

def Pow(x, n):
    def helper(x, n):
        # Base Case
        if x == 0:
            return 0
        if n == 0:
            return 1
        if x == 1:
            return 1

        # x * x^2 * x^2 = x^5
        res = helper(x, n//2)
        res *= res
        return x * res if x % 2 != 0 else res

    res = helper(x, abs(n))
    if res == 0 and n >= 0:  # check for infinity, for you, n is y
        return Exception('Division by zero error')
    return res if n >= 0 else 1/res


print(pow(2, 3))


# Iterative

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n
        s = 1
        m = n
        n = abs(m)

        while(n > 1):
            if(n % 2 == 0):
                x = x*x
                n = n//2
            else:
                s = s*x
                n = n-1
        s = s*x
        if(m > 0):
            return(s)
        elif(m == 0):
            return(1)
        else:
            return(1/s)
