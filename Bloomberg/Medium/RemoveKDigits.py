

class Solution:
    def removeKdigits(self, num: str, k: int) -> str: 
        i, n = 0, len(num)
        stack = []
        
        # 1 7 9 4 2     Try to keep increment
        # 1 7 4
        # 1 4
        
        if k >= n:
            return "0"
        
        while (i < n):
            while (stack and k > 0 and int(stack[-1]) > int(num[i])):
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
            
        while k > 0:
            stack.pop()
            k -= 1
        # remove leading zeros
        return str(int("".join(stack)))
        