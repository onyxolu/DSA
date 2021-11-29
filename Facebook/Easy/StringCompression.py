
# Two pointers

from collections import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Two pointers , i,j to know how many times a char occurs
        # j-i = how many times it occurs and push ["a", "2"]
        # move i to j and continue
        # edge case ["a", "b", "12"] => ["a", "b", "1", "2"]
        # idx - to build my result string
        # i keep track of last compression
        # j keep track of nu of repeats
        
        idx, i = 0,0
        while i < len(chars):
            j = i
            # aaaabbbbb  increment j from 0 to when a stops
            while j < len(chars) and chars[j] == chars[i]:
                j +=1
            
            chars[idx] = chars[i]
            idx += 1
            if j - i > 1: # frequency of the char
                count = str(j-i)
                for c in count: # add each char in freq 
                    chars[idx] = c
                    idx += 1
            i = j # continue from next letter after repetition (b)
            
        return idx
        