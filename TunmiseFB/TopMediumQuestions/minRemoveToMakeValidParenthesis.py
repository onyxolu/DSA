'''
The parentheses in a string are balanced if and only if these 2 conditions are met:

1. We have the same number of "(" and ")" in the string.
2. Scanning through the string from left to right and counting how many "(" and ")" there are so far, 
there should never be a time where there are more ")" than "(". We call count("(") - count(")") the balance 
of the string..

We could use a stack Stack 0(N).

When we come across the open tag, I append its index to a stack, then if I come across a close tag, 
I pop something from the stack, if the stack is empty, I simply replace that closing tag at that index 
with an empty value.
That way at the end of the day we're left with a list of all the indexes we want to pop off.
At the end we have a list that will be balanced, so we convert it back to atring and return it.

Time complexity - O(N)
Space - O(N) because of the stack
'''

class Solution:
    def minRemoveToMakeValid(s):
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




