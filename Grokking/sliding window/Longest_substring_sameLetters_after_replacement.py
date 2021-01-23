 
str = "aabccbb"

def longest_substring_same_characters(s, k):
    max_length = 0
    max_length_repete = 0
    window_start = 0
    freqeuncy_dic = {}
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in freqeuncy_dic:
            freqeuncy_dic[right_char] = 0 
        freqeuncy_dic[right_char] += 1
        max_length_repete = max(max_length_repete, freqeuncy_dic[right_char])

        if (window_end - window_start + 1 - max_length_repete) > k:
            left_char = s[window_start]
            freqeuncy_dic[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length 

print(longest_substring_same_characters(str, 2))