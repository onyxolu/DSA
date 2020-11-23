def titleToNumber(s):
    n = len(s) - 1
    sheetNo = 0
    for i in range(len(s)):
        sheetNo += (ord(s[i]) - ord("A") + 1) * (26)**(n-i)
    return sheetNo

print(titleToNumber("AA"))