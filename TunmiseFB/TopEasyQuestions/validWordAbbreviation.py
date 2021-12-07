'''

Idea:
    Iterate through the abbr.

    If we encounter a letter, then we check if the curr index on the word equals the letter.
        If letters do not match, then the abbr is not valid.
        
    If we encounter a number, then we progress the curr index of the word by that number.
        If the index exceeds the possible indices on the word, then abbr is not valid.

'''


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wi = 0
        
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        curr_num = ""
        for c in abbr:
            # Note: need to account for beginning zero
            if c in digits and not (c == "0" and not curr_num):
                # We have encountered a number that is not a leading zero
                curr_num += c
            else:
                # We have encountered a letter or a leading zero (treated as a character)
                
                # If there is a number, progress the word pointer
                if curr_num:
                    wi += int(curr_num)
                    curr_num = ""
                # Check if we have exceeded the length of the word OR
                # if the current word character is not equal to the abbr character
                if wi >= len(word) or not word[wi] == c: 
                    return False
                # Progress the word pointer
                wi += 1
        
        # Need to account for a number at the end of abbr
        if curr_num:
            wi += int(curr_num)
        # Need to check that we have traversed the entire word
        if wi != len(word): return False
        
        # All checks pass, the abbr is valid
        return True