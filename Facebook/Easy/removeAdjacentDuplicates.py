# stack

def removeAdjDuplicates(s):
    stack = []
    for val in s:
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)

    return "".join(stack)