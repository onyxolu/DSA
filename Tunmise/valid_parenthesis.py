class Solution:
    def isValid(self, s: str) -> bool:
        stack,lookup = [],{"[":"]","(":")","{":"}"}
        
        for i in s:
            if i in lookup:
                stack.append(i)
            elif not stack or lookup[stack.pop()] != i:
                return False
        return len(stack) == 0