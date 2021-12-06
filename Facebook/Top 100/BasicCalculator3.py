

# The Algorithm:

# Put all the numbers with their correct sign into the stack.
# Put '(' and the operator before that into the stack.
# If we see the ')', pop from the stack until we get to '('. Update the num by the evaluated amount inside the parentheses and the operator before '('.


class Solution:
    def calculate(self, s: str) -> int:
        
        op, num, stack='+', 0, []
        for c in s+'+':
            if c==' ': continue
            if c in '0123456789':
                num= num*10 + int(c)
            
            elif c=='(':
				# Push op and '(' to the stack
                stack.append(op)
                stack.append(c)
                op='+'
            
            elif c==')':
				# Given op, we put the current number to tmp
                if op=='*':
                    tmp=stack.pop() * num
                elif op=='/':
                    tmp=int(stack.pop() / num)
                else:
                    tmp= num if op=='+' else -num
                
				# Add the elements in stack utill '('.
                while stack[-1]!='(':
                    tmp+=stack.pop()
                stack.pop()   # pop '('
                
				# update the num having the op before '('.
                if stack[-1]=='*':
                    stack.pop()
                    num=stack.pop() * tmp 
                elif stack[-1]=='/':
                    stack.pop()
                    num=int(stack.pop() / tmp )
                else:
                    num=tmp if stack.pop()=='+' else -tmp
                op='+'
            
            else:
				# Given op, update the current number.
                if op=='*':
                    stack.append(stack.pop() * num)
                elif op=='/':
                    stack.append(int(stack.pop() / num) )
                else:
                    stack.append( num if op=='+' else -num )
                num, op = 0, c
        
        return sum(stack)