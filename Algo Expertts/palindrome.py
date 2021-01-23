
def allPalindromes(s):
    ans = 0
    for i in range(0, len(s)):
        getPalindromeFrom(s, i-1, i+1, ans)
        getPalindromeFrom(s, i-1, i, ans)
        
def getPalindromeFrom(str, leftIdx, rightIdx, ans):
    while leftIdx >= 0 and rightIdx < len(str):
        if str[leftIdx] != str[rightIdx]:   
            break
        leftIdx -=1
        rightIdx +=1

    print(str[leftIdx + 1: rightIdx], leftIdx, rightIdx)

    


print(allPalindromes("aaaaa"))







def threatDetector(textMessages):
    # input is array of strings
    # Loop through array and get each string
    # Do a Palindrome check with an helper function
    # compile report and push to ans array
    # Write your code here
    
    ans = []
    for val in textMessages:
        find_palindrome(val, ans)
       
    return ans
        
def find_palindrome(str, ans):
    str_length = len(str)

    symbol = str[str_length - 3: str_length]
    strVal = str[0: str_length - 3]
    strVal.lower()
    
    valid_palindromes = 0
    for i in range(1, len(str)):
        odd = getPalindromeFrom(strVal, valid_palindromes, i-1, i+1)
        even = getPalindromeFrom(strVal, valid_palindromes, i-1, i)
        
        if odd:
            valid_palindromes += odd
        if even:
            valid_palindromes += even
        
    if(valid_palindromes >= 1 and valid_palindromes <= 10):
        threat = symbol + " " + "Possible"
        print(threat)
    elif(valid_palindromes >= 11 and valid_palindromes <= 40):
        threat = symbol + " " + "Probable"
        print(threat)
    elif(valid_palindromes >= 41 and valid_palindromes <= 150):
        threat = symbol + " " + "Escalate"
        print(threat)
    else:
        threat = symbol + " " + "Ignore"
        print(threat)
        
def getPalindromeFrom(str, valid_palindromes, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(str):
        if str[leftIdx] != str[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    
    if (rightIdx - (leftIdx+1) >= 3):
        return rightIdx - (leftIdx+1)