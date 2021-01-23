
str = "abcabcbb"

def no_repeat(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length



# def no_repeat(s):
#     dict = {}
#     maxStr = 0
#     windowValue = "" 
#     for windowKey in range(len(s)):
#         currentStr = s[windowKey]
#         windowValue += currentStr
#         if(currentStr in dict):
#             dict[currentStr] += 1
#         else: 
#             dict[currentStr] = 1

#         if max(dict.values()) > 1:
#             firstLetter = windowValue[0]
#             if dict[firstLetter] > 1:
#                 dict[firstLetter] -= 1
#             else:
#                 del dict[firstLetter]
#             windowValue = windowValue[1:]
#         else: 
#             maxStr = max(len(windowValue), maxStr)


#     return maxStr


print(no_repeat(str))