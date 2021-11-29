
# Hashmap Solution

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        allienDict = {}
        for i in range(len(order)):
            allienDict[order[i]] = i
            
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                if len(w2) - 1 < j:
                    return False
                if allienDict[w1[j]] < allienDict[w2[j]]:
                    break
                if allienDict[w1[j]] > allienDict[w2[j]]:
                    return False
                
        return True