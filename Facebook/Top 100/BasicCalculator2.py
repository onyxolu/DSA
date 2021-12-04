
import math

# Stack

# input = 11 -5 + 4*3 +12/6
# we add numbers and handle - like 11+(-5)
# for multiply and divide, we pop the number off our stack and append the multiplied figure
# 11+(-5) + 12 + 2


class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, "+", []
        for i in s+"+": #we put + to handle adding the final val
            if i.isdigit():
                num = num*10 + int(i)
            elif i in "+-*/":
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop()*num)
                if sign == "/":
                    stack.append(math.trunc(stack.pop()/num))
                    # Math.trunc() function returns the integer part of a number by removing any fractional digits
                sign = i
                num = 0
        return sum(stack)