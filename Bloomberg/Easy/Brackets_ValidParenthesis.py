
# Balanced Brackets
# Time Complexity = 0(N)
# Space Complexity = 0(N)

# Stack - Order of opening brackets

def isValid(s):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingChar = {")": "(", "]": "[", "}": "{"}
    stack = []
    for val in s:
        if val in openingBrackets:
            stack.append(val)
        elif val in closingBrackets:
            if len(stack) == 0:
                return False
            lastItem = stack[-1]
            if lastItem == matchingChar[val]:
                stack.pop()
            else: 
                return False
    return len(stack) == 0

print(isValid("()[]{}"))