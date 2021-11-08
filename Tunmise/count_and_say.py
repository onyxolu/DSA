class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            stack = []
            s =self.countAndSay(n-1)
            stack.append([s[0],1])
            for i in range(1,len(s)):
                if s[i] == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([s[i],1])
            l = []
            for char,count in stack:
                l.append(str(count)+char)
            return "".join(l)

sl = Solution()
print(sl.countAndSay(1))
print(sl.countAndSay(2))
print(sl.countAndSay(3))
print(sl.countAndSay(4))
print(sl.countAndSay(5))