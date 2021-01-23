
s = "cbaebabacd"
p = "abc"

def findAnagrams(s, p):
    window_start = 0
    char_frequency = {}
    matched_indices = []
    matched = 0
        
    for val in p:
        if val not in char_frequency:
            char_frequency[val] = 0
        char_frequency[val] += 1
            
    for window_end in range(len(s)):
        currentVal = s[window_end]
        window_length = window_end - window_start + 1
        if currentVal in char_frequency:
            char_frequency[currentVal] -= 1
            if char_frequency[currentVal] == 0:
                matched += 1
                    
        if matched == len(char_frequency):
            matched_indices.append(window_start)
                
        if window_length >= len(p):
            left_char = s[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            window_start += 1
    return matched_indices

print(findAnagrams(s,p))