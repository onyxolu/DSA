class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
        
        while stack:
            remove_indices.add(stack.pop())
        
        for index, char in enumerate(s):
            if index not in remove_indices:
                stack.append(char)
        
        return ''.join(stack)