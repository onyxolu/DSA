def camelCase(words):
    result = ""
    for index in range(len(words)):
        word = words[index]
        
        if not result or word == " " or result[-1] == " ":
            result += word.lower()
        else:
            result += word.capitalize()
    return result

s = ["BOY","i","i","girl","swIM"]

import sys
words = []
for line in sys.stdin:
    words.append(line[:-1])
y=[]
print(y)




print(camelCase(s))


def isSelfDescribing(n):
    s = str(n)
    return all(s.count(str(i)) == int(ch) for i ,ch in enumerate(s))

for line in sys.stdin:
    if isSelfDescribing(line.strip()):
        print("1")
    else:
        print("0")