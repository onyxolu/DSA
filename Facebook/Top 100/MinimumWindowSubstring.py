
# Sliding window

# TC - O(N+M)
# SC - 0(M)

# We will keep a running count of every matching instance of a character.

# Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.

# We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the window.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # matched - count every matching of a xter
        win_start, matched, substr_start = 0,0,0
        min_len = len(s) + 1
        freq = Counter(t)
        
        for win_end in range(len(s)):
            right_char = s[win_end]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] >= 0:
                    matched += 1
                    
            # shrink the window if we can, finish as soon as we remove a matched xter
            while matched == len(t):
                win_len = win_end - win_start + 1
                if min_len > win_len:
                    min_len = win_len
                    substr_start = win_start
                    
                left_char = s[win_start]
                win_start += 1
                if left_char in freq:
                    if freq[left_char] == 0:
                        matched -= 1
                    freq[left_char] += 1
        return "" if min_len > len(s) else s[substr_start: substr_start + min_len]
        