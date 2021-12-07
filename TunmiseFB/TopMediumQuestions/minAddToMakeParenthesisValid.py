'''

Approach 1: Balance

Intuition and Algorithm

Keep track of the balance of the string: the number of '(''s minus the number of ')''s. A string is valid if its balance is 0, plus every prefix has non-negative balance.

The above idea is common with matching brackets problems, but could be difficult to find if you haven't seen it before.

Now, consider the balance of every prefix of S. If it is ever negative (say, -1), we must add a '(' bracket. Also, if the balance of S is positive (say, +B), we must add B ')' brackets at the end.


Time Complexity: O(N), where N is the length of S.

Space Complexity: O(1).

'''

class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal




'''

STACK APPROACH

'''

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        _stack=[]                                #initilized a new stack
        for bracket in S:                        # looping through all the brackets in S, storing each in bracket variable
            if(len(_stack)==0):                  # checking if the stack is empty then
                _stack.append(bracket)           # push the bracket to the empty stack
            else:                                # else
                curr=_stack[len(_stack)-1]       #storing the top of the stack to the curr variable
                if curr =='(' and bracket ==')': #checking if the curr has opening and the bracket has closing bracket then the bracket from the stack is poped 
                     _stack.pop()
                else:                            # else the bracket will be added to the stack
                    _stack.append(bracket)
                    
        return len(_stack)                       #returning the lenght of the stack - it contains all the invalid paranthesis 
