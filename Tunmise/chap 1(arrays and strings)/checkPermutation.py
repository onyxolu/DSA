def checkPermutation(s1,s2):
    asciiValue1 = getAsciiValue(s1)
    asciiValue2 = getAsciiValue(s2)

    if asciiValue1 == asciiValue2:
        return True
    else:
        return False

def getAsciiValue(s):
    total = 0
    for char in s:
        total += ord(char)
    return total
