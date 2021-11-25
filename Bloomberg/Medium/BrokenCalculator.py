
# if we do multiply and subtract, edge cases dey and it won't fly

# why not do reverse, divide and add - That will work

# key is we need to always divide first before adding to get minimum 



# conditions
#  x == y
#  y < x   #our solution
#  y > x   # we can't multiply, we can only subtract


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2 == 0:
                target /= 2
            else:
                target += 1
                
        return int(res + startValue - target)