# Time Complexity = 0(N)
# Space Complexity = 0(N)

# hashMap

def firstUniqueChar(s):
    freq = {}
    for val in s:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1
    for i in range(len(s)):
        val = s[i]
        if freq[val] == 1:
            return i
        
    return -1




# ord, chr



NO_OF_CHARS = 256
 
'''
The function returns index of the first
non-repeating character in a string. If
all characters are repeating then
returns INT_MAX '''
 
def firstNonRepeating(string):
    #initialize all character as absent
     
    arr=[-1 for i in range(NO_OF_CHARS)]
     
    '''
    After below loop, the value of
    arr[x] is going to be index of
    of x if x appears only once. Else
    the value is going to be either
    -1 or -2.'''
     
    for i in range(len(string)):
        if arr[ord(string[i])]==-1:
            arr[ord(string[i])]=i
        else:
            arr[ord(string[i])]=-2
    res=10**18
     
    for i in range(NO_OF_CHARS):
        '''
        If this character occurs only
        once and appears before the
        current result, then update the
        result'''
        if arr[i]>=0:
            print(i, arr[i], res, string[arr[i]])
            res=min(res,arr[i])
    return res
 
#Driver prohram to test above function
 
string="leetcode"
 
index=firstNonRepeating(string)
 
if index==10**18:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is",string[index])
 


firstUniqueChar("leetcode")
