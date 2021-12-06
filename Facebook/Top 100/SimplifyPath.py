
# Stack

# We use a stack bcos of double dot to easily pop

# ignore slatch and double dots
# for "/home//foo/"
# stack = ["home", "foo"]

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""     
            else:
                cur += c
        return "/" + "/".join(stack)
        