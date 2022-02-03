
# Recursive Solution is the first intuitive way cos its nested and there are sub problems

# 54[abd[cd]]
# Stack = [5,4,[, a,b,6,[, c,d,]
# [5,4,[, a,b]   6cd


def decodeString(self, s: str) -> str:
    stack = []
    for val in s:
        if val != "]":
            stack.append(val)
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr  # get the substring
            stack.pop()  # pop the [
            num = ""
            while stack and stack[-1].isdigit():  # get the number
                num = stack.pop() + num
            stack.append(int(num) * substr)

    return "".join(stack)


# Recursive

class Solution(object):
    def decodeString(self, s):
        s = list(s)[::-1]

        def helper():
            ans = []
            k = 0
            while s:
                char = s.pop()
                if char.isalpha():
                    k = 0
                    ans.append(char)
                elif char.isnumeric():
                    k = k * 10 + int(char)
                elif char == '[':
                    res = helper()
                    ans.append(res * k)
                    k = 0
                elif char == ']':
                    return ''.join(ans)
            return ''.join(ans)

        return helper()
