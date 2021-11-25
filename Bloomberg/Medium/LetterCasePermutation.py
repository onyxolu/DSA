

class Solution:
    def letterCasePermutation(self, s: str):
        # Time = (2^N)*(N)
        output = [""]
        
#         [''] ['a', 'A']
# ['a', 'A'] ['a1', 'A1']
# ['a1', 'A1'] ['a1b', 'a1B', 'A1b', 'A1B']
# ['a1b', 'a1B', 'A1b', 'A1B'] ['a1b2', 'a1B2', 'A1b2', 'A1B2']

        
        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o+c.lower())
                    tmp.append(o+c.upper())
            else:
                for o in output:
                    tmp.append(o+c)
            output = tmp
            
        return output


class Solution:
    def letterCasePermutation(self, s: str):
        op=[]
        def form(i,s,p):
            if i==S:
                op.append(p)
                return
            if s[i].isdigit():
                form(i+1,s,p+s[i])
            else:
                form(i+1,s,p+s[i].lower())
                form(i+1,s,p+s[i].upper())

        S=len(s)
        form(0,s,"")
        return op