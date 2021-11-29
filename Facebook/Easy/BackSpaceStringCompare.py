
# Stack

# add the two strings in separate stacks
# when you see # you pop
# edge case, check empty stack before pop

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for val in s:
            if val == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(val)
                
        for val in t:
            if val == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(val)
        return stack1 == stack2
        



# Two Pointers

# 


class Solution(object):
    def backspaceCompare(self, s, t):
        i,j = len(s)-1, len(t)-1
        sDelete, tDelete = 0, 0
		
        while True:
            if i<0 and j<0:
                return True
				
            checkT, checkS = True, True
			
            if i >= 0:
                if s[i] == "#":
                    sDelete, i, checkS = sDelete+1, i-1, False
                elif sDelete:
                    sDelete, i, checkS = sDelete-1, i-1, False
            if j >= 0:
                if t[j] == "#":
                    tDelete, j, checkT = tDelete+1, j-1, False
                elif tDelete:
                    tDelete, j, checkT = tDelete-1, j-1, False
                    
            if checkS and checkT:
                if i<0 or j<0:
                    return False
                if s[i] != t[j]:
                    return False
                i-=1
                j-=1