
# Time Complexity => 0(N)

def addDigits(num):
    if num < 10:
        return num
    while num > 9:
        numStr = str(num)
        numSum = 0
        for val in numStr:
            numSum += int(val)
        num = numSum
    return num

# Time Complexity => 0(1)
def addDigits(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num%9

9-9
10-1
11-2
12-3
...
18-9
19-1
20-2

27-9
...
30-3
31-4
32-5

36-9
...
40-4
41-5
42-6

45-9
...
50-5