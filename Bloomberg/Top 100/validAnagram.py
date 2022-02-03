# Time Complexity = 0(N)
# Space Complexity = 0(N)

# Hashmap

def validAnagram(s, t):
    sFreq = {}
    tFreq = {}
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        sVal = s[i]
        tVal = t[i]
        if sVal in sFreq:
            sFreq[sVal] += 1
        else: sFreq[sVal] = 1
            
        
        if tVal in tFreq:
            tFreq[tVal] += 1
        else: tFreq[tVal] = 1
            
    return sFreq == tFreq