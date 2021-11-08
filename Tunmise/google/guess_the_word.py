from typing import DefaultDict


class Solution:
    def findSecretWord(self, wordlist,master) -> None:
        #get match words
        def getMatch(w, words, match):
            res = []
            for word in words:
                if w == word: continue
                if sum([1 for i in range(6) if w[i] == word[i]]) == match:
                    res.append(word)
            return res
        
        #get most common word
        def getMaxCom(words):
            comm = [0] * len(words)
            for i in range(6):
                com_dict = DefaultDict(int)
                for w in words:
                    com_dict[w[i]] += 1
                for j, w in enumerate(words):
                    comm[j] += com_dict[w[i]]
            max_com, res = 0, []    
            for i, v in enumerate(comm):
                if v > max_com:
                    max_com = v
                    res = [words[i]]
                elif comm[i] == max_com:
                    res.append(words[i])
            return res
        
        times, com_list = 0, []
        
        while times < 10:
            com_list += getMaxCom(wordlist)
            try_string = com_list.pop()
            match = master.guess(try_string)
            if match == 6: return try_string
            wordlist = getMatch(try_string, wordlist, match)
            times += 1
            
        return