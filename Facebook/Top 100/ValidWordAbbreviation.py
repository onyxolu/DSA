
# Two pointers
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0
        
        while p1 < len(word) and p2 < len(abbr):
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            else:
                if abbr[p2].isdigit():
                    if abbr[p2] == '0': # has leading zeros
                        return False
                    else:
                        d = abbr[p2]
                        p2 += 1
                        while p2 < len(abbr) and abbr[p2].isdigit():
                            d += abbr[p2]
                            p2 += 1
                        
                        p1 += int(d)
                else:
                    return False

        return True if (p1 == len(word)) and (p2 == len(abbr)) else False