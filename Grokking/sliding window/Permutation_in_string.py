
s1 = "ab"
s2 = "eidbaooo"


def checkInclusion(s1,s2):
    window_start = 0
    matched = 0
    frequency_pattern_map = {}
    for val in s1:
        if val not in frequency_pattern_map:
            frequency_pattern_map[val] = 0
        frequency_pattern_map[val] += 1
            
    for window_end in range(len(s2)):
        window_length = window_end - window_start + 1
        right_char = s2[window_end]
        if right_char in frequency_pattern_map:
            frequency_pattern_map[right_char] -= 1
            if frequency_pattern_map[right_char] == 0:
                matched += 1
                    
        if matched == len(frequency_pattern_map):
            return True
            
        if window_length >= len(s1):
            left_char = s2[window_start]
            window_start += 1
                
            if left_char in frequency_pattern_map:
                if frequency_pattern_map[left_char] == 0:
                    matched -= 1
                frequency_pattern_map[left_char] += 1
    return False


print(checkInclusion(s1, s2))