def int2string(num):
    is_negative = False
    if(num == 0):
        return "0"
    if num < 0:
        is_negative = True
        num *= -1
    
    s = ""
    while num > 0:
        s = chr(ord("0") + num % 10) + s
        num //= 10
    
    if is_negative:
        return "-" + s
    else:
        return s



def string2int(s):
    is_negative = False
    if s[0] == "-":
        is_negative = True
        s = s[1::]
    ans = 0
    for i in range(len(s)):
        num = ord(s[i]) - ord("0")
        ans += num * 10 ** (len(s)-1-i)

    if is_negative:
        return ans*-1
    return ans



print(int2string(499)) 
print(int2string(-15)) 
print(string2int("1876")) 