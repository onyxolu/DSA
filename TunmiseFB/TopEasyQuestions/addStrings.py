'''
SOLUTION:
Create a custom function to convert the number from string to integer.
Use a dictionary to compare values. Apply the concept of unit, tens and hundred to convert 
the string to integer and add.
output = output * 10 + number, starting from output = 0
Add the two interger and the convert to string and return 
'''


def addStrings(num1, num2):
    
    def str2int(num):
        numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        output = 0
        for d in num:
            output = output * 10 + numDict[d]
        return output
    
    return str(str2int(num1) + str2int(num2)) 


'''
Method 2: Simulate carry operation in Maths

Digit-by-digit addition.

Algorithm

1. Initialize an empty res structure. Once could use array in Python and StringBuilder in Java.

2. Start from carry = 0.

3. Set a pointer at the end of each string: p1 = num1.length() - 1, p2 = num2.length() - 1.

4. Loop over the strings from the end to the beginning using p1 and p2. Stop when both strings are used entirely.

    -   Set x1 to be equal to a digit from string nums1 at index p1. If p1 has reached the beginning of nums1, set x1  to 0.
    
    -   Do the same for x2. Set x2 to be equal to digit from string nums2 at index p2. If p2 has reached the beginning of nums2, set x2 to 0.
    
    -   Compute the current value: value = (x1 + x2 + carry) % 10, and update the carry: carry = (x1 + x2 + carry) / 10.
    
    -                                                                           ````             Append the current value to the result: res.append(value).

5. Now both strings are done. If the carry is still non-zero, update the result: res.append(carry).

6. Reverse the result, convert it to a string, and return that string.

'''

# Simulate the math addition
# Start from the back to simulate normal addition from the back
# Handle carry
# return res

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
