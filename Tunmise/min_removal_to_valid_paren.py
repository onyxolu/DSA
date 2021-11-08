def minRemovalToMakeValid(s):
    hs = set()
    stack =[]
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if len(stack)== 0:
                hs.add(i)
            else:
                stack.pop()
    while len(stack) != 0:
        hs.add(stack.pop())
    l = []
    for i in range(len(s)):
        if i not in hs:
            l.append(s[i])
    return "".join(l)
