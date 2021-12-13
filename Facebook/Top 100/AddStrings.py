
# Two pointers

# 456
# +
#  77
# ---
# 533
# ---

def addStrings(num1, num2):
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    while (i >= 0 or j >= 0):
        sum = carry
        if i >= 0:
            sum += ord(num1[i]) - ord('0')
        if j >= 0:
            sum += ord(num2[j]) - ord('0')
        result = str(sum % 10) + result
        carry = int(sum / 10)
        print(sum, result, carry)
        i -= 1
        j -= 1

    if carry != 0:
        result = str(carry) + result

    return result


print(addStrings("456", "77"))