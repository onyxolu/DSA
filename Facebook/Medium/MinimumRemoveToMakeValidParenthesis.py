
# Stack 0(N)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
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
                    S[i] = "" # remove closing bracket
        # stack contains all idx of open parenthesis we want to pop off
        for j in stack:
            S[j] = ""
            
        return "".join(S)









class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
                # We need variable 'current', in order to keep track of how many open or closed brackets left
        # If 'current' equals 0, then we don't append ')' to 'stack'. Meaning: there is no open bracket to close 
        current = 0
        stack = []

        for string in s:
            if string not in '()':
                stack.append(string)
            else:
                if string == '(':
                    stack.append(string)
                    current += 1

                # If 'current' equals 0, then we don't append ')' to 'stack'
                elif string == ')':
                    if current > 0:
                        stack.append(string)
                        current -= 1

        # In case we have some open braces, then we have to delete them from 'stack'
        # If 'current' is greater than zero, it means we have some open braces left, without closed braces
        if current > 0:

            # We have to reverse the 'stack', in order to delete the open braces from the end of the 'stack'
            stack.reverse() # so I can Remove from the end [(()))] => [(())]
            while current != 0:
                stack.remove('(')
                current -= 1

            # Reverse the 'stack' back to original status
            stack.reverse()
        s = ''.join(stack)
        return s
