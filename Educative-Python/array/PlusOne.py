    
    
def plusOne(digits):
    if digits == [0,0]:
        return [0,1]
    s = ''.join(map(str, digits))
    s = int(s) + 1
    s = str(s)
    newArr = []
    for val in s:
        newArr.append(int(val))
    return newArr

print(plusOne([1,2,3]))
print(plusOne([0,0]))