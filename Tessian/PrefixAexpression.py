
# Python3 program to evaluate a prefix expression.
def isdigit(ch):
    if(ord(ch) >= 48 and ord(ch) <= 57):
        return True
    return False


def evaluatePrefix(exprsn, dict):
    Stack = []

    for j in range(len(exprsn) - 1, -1, -1):

        # if jth character is the delimiter ( which is
        # space in this case) then skip it
        if (exprsn[j] == ' '):
            continue

        # Push operand to Stack
        # To convert exprsn[j] to digit subtract
        # '0' from exprsn[j].
        if (isdigit(exprsn[j])):

            # there may be more than
            # one digits in a number
            num, i = 0, j
            while (j < len(exprsn) and j >= 0 and isdigit(exprsn[j])):
                j -= 1
            j += 1

            # from [j, i] exprsn contains a number
            for k in range(j, i + 1, 1):
                num = num * 10 + (ord(exprsn[k]) - ord('0'))

            Stack.append(num)
        elif exprsn[j] in "+-*/":
            if exprsn[j+1] != " ":
                return None
            if j != 0 and exprsn[j-1] != " ":
                return None
            # Operator encountered
            # Pop two elements from Stack
            if Stack:
                o1 = Stack[-1]
                Stack.pop()
            else:
                return None

            if Stack:
                o2 = Stack[-1]
                Stack.pop()
            else:
                return None

            # Use switch case to operate on o1
            # and o2 and perform o1 O o2.
            if exprsn[j] == '+':
                Stack.append(o1 + o2)
            elif exprsn[j] == '-':
                Stack.append(o1 - o2)
            elif exprsn[j] == '*':
                Stack.append(o1 * o2)
            elif exprsn[j] == '/':
                Stack.append(o1 / o2)

        elif exprsn[j] in dict:
            Stack.append(dict[exprsn[j]])

    return Stack[-1] if len(Stack) == 1 else None


# exprsn = "+ 1 5" "+ 1 2 3" "+ 1" "9" "* + 1 2 3" "-+ 1 5 3"
exprsn = "* + 2 x y"
dict = {
    "x": 1,
    "y": 3
}
print(evaluatePrefix(exprsn, dict))

# This code is contributed by divyesh072019.
