# stack

def removeAdjDuplicates2(s, k):
    stack = []
    for val in s:
        if stack and stack[-1][0] == val:
            stack[-1][1] += 1
        else:
            stack.append([val, 1])
        
        if stack[-1][1] == k:
            stack.pop()

    return "".join([ val * f for val,f in stack])


print(removeAdjDuplicates2("deeedbbcccbdaa", 3))