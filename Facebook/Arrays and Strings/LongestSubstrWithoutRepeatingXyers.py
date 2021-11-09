# Sliding Window
# hashmap => key = xter , value = i

def lengthOfLongestSubstring(s: str) -> int:
    
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        print(s[window_start: window_end], char_index_map)
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(lengthOfLongestSubstring("abcabcbb"))

# a {a:0} 1
# ab {a:0, b:1} 2
# abc {a:0, b:1, c:2 } 3
# abca, bca {a:3, b:1, c:2} 3
# abcab, cab {a:3, b:4, c:2} 3
# abcabc, abc {a:3, b:4, c:5} 4


# "abba"
#a {a:0}
#ab {a:0, b:1}
#abb, b {a:0, b:2}
#abba, ba