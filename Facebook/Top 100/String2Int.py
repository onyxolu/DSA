# ord - ASCII

def myAtoi(s):
    s = s.strip() # removes whitespace at the beginning and end
    if not s:
        return 0
    negative = False
    out = 0
    minVal = -2**31
    maxVal = 2**31 - 1

    if s[0] == "-":
        negative = True
    elif s[0] == "+":
        negative = False
    elif not s[0].isnumeric():
        return 0
    else:
        out = ord(s[0]) - ord("0")
    for i in range(1, len(s)):
        if s[i].isnumeric():
            out = out*10 + (ord(s[i]) - ord("0"))
            if not negative and out >= maxVal:
                return maxVal
            if negative and out > maxVal:
                return minVal
        else:
            break
    if not negative:
        return out
    else:
        return -out


print(myAtoi("4193 with words"))