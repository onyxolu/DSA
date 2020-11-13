def getFact(num):
    fact = 1
    while num > 0:
        fact *=num
        num-=1

    return fact

print(getFact(2))


def getFactR(num):
    if num == 1:
        return 1

    return (num) * getFactR(num-1)

print(getFactR(5))



