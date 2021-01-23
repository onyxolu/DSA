s = "abdabca" 
t = "abc"


def minWindow( s , t):
    min_length = len(s) + 1
    substr_start = 0
    window_start = 0
    frequency_char = {}
    matched = 0
    
    for val in t:
        if val not in frequency_char:
            frequency_char[val] = 0
        frequency_char[val] += 1
        
    for window_end in range(len(s)):
        currentVal = s[window_end]
        
        if currentVal in frequency_char:
            frequency_char[currentVal] -= 1
            if frequency_char[currentVal] >= 0:
                matched += 1   
    
        
        while matched == len(t):
            window_length = window_end - window_start + 1
            if min_length > window_length:
                min_length = window_length
                substr_start = window_start
                
            left_val = s[window_start]
            window_start += 1
            if left_val in frequency_char:
                if frequency_char[left_val] == 0:
                    matched -= 1
                frequency_char[left_val] += 1
    
    if min_length > len(s):
        return ""
    return s[substr_start: substr_start + min_length]

print(minWindow(s, t))