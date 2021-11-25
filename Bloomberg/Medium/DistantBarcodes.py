

# Two Pointers solution won't work for [2,1,1] 

# [1,2,1,2,1,2] at most we will have n/2 freq of a number e.g 1 occuring 3 times
# [1,2,1,2,1] or at most n+1/2


from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes):
        if not barcodes:
            return barcodes
        
        # create counter
        freq = Counter(barcodes)
        
        # identify max occuring element
        maxNum = max(freq, key=freq.get)
        maxFreq = freq[maxNum]
        
        #create result array and fill with zeros
        result = [0] * len(barcodes)
        
        #start  filling list with most frequently occuring element
        idx = 0
        for _ in range(maxFreq):
            result[idx] = maxNum
            idx += 2
            
        # fill out odd indexes with rest of elements
        del freq[maxNum]
        if idx >= len(result):
            idx = 1
            
        for num in freq:
            numFreq = freq[num]
            while numFreq > 0:
                result[idx] = num
                idx += 2
                numFreq -= 1
                if idx >= len(result):
                    idx = 1
            
        return result
            