
# Stack

# (1+(4+5+2)-3)+(6+8)

class Solution:
    def calculate(self, s: str) -> int:
        output, cur, sign, stack = 0,0,1,[]
        
        for c in s:
            if c.isdigit():
                cur = cur*10 + int(c)
            elif c in "+-":
                output += (cur*sign)
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ")":
                output += (cur*sign)
                output *= stack.pop() # pop sign and mulltiply by sign
                output += stack.pop() # pop last output and add 
                cur = 0
            print(stack)
        return output + (cur*sign)
        