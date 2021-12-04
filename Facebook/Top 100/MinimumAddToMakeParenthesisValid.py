
# Stack

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []
        n = len(s)
        S = list(s)
        
        for i in range(n):
            if S[i] == "(":
                stack.append(i) # keep track of index of open bracket
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    res += 1 
                    S[i] = "" # remove closing bracket
        # stack contains all idx of open parenthesis we want to pop off
        for j in stack:
            res += 1
            S[j] = ""
            
        return res