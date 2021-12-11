from collections import List
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        #try start with every index of s to match every word in words, record the start and end position in the s if matches any words
        #merge the intervals of the start end pair to remove the overlaps
        #add the bold tag before the start and after the end indices
        
        #O(n*m) time, O(n) space, n is the length of the string, m is the total length of the strings in the words
        
        intervals = []
        for start in range(len(s)):
            for word in words:
                if s[start:].startswith(word):
                    end = start+len(word)
                    if intervals and intervals[-1][1] >= start:
                        intervals[-1][1] = max(intervals[-1][1], end)
                    else:
                        intervals.append([start, end])
        array = []
        prevEnd = 0
        for start, end in intervals:
            array.append(s[prevEnd:start])
            array.append("<b>"+s[start:end]+"</b>")
            prevEnd = end
            
        if prevEnd < len(s):
            array.append(s[prevEnd:])
        
        return "".join(array)



# Using Flag
# "aaabbcc" , [aaa, aab, bc] => [1111110]
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        flag = [0] * n
        cur_end = 0
        for i in range(n):
            for w in words:
                if s.startswith(w, i):
                    cur_end = max(cur_end, i + len(w))
                    
                flag[i] = i < cur_end
        ans = ""
        
        for i in range(n):
            if flag[i] and (i == 0 or (i > 0 and not flag[i-1])):
                ans += "<b>"
                
            ans += s[i]
            
            if flag[i] and (i == n-1 or (i < n-1 and not flag[i+1])):
                ans += "</b>"
                
        return ans