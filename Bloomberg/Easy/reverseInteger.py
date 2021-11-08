
# Modulus

def reverseInteger(num):
    negative = False
    if num < 0:
        negative = True
        num = -num
    MIN = -(2**31)
    MAX = (2**31) - 1
    res = 0
    while num > 0:
        digit = int(num % 10)
        num = int(num/10)
        if res > MAX or res < MIN:
            return 0
        res = res*10 + digit
    return -res if negative else res 


print(reverseInteger(123))