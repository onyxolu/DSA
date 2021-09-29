def largestCharacter(str):
     
    # Array for keeping track of both uppercase
    # and lowercase english alphabets
    uppercase = [False] * 26
    lowercase = [False] * 26
     
    arr = list(str)
    for c in arr:
        if (c.islower()):
            lowercase[ord(c) - ord('a')] = True
        if (c.isupper()):
            uppercase[ord(c) - ord('A')] = True
             
    # Iterate from right side of array
    # to get the largest index character
    for i in range(25,-1,-1):
         
        # Check for the character if both its
        # uppercase and lowercase exist or not
        if (uppercase[i] and lowercase[i]):
            return chr(i + ord('A')) + ""
    # Return -1 if no such character whose
    # uppercase and lowercase present in
    # string str
    return "-1"
 
# Driver code
 
str = "admeDCAB"
print(largestCharacter(str))