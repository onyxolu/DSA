from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        # the UTF8 is at most 4 bytes long
        # so the first bit is at most 4 1
        
        count = 0 # count # of byte remaining
        
        for num in data:
            
            if count == 0:
                
                if num < 0x80: continue
                elif (num & 0xE0) == 0xC0: count = 1
                elif (num & 0xF0) == 0xE0: count = 2
                elif (num & 0xF8) == 0xF0: count = 3
                else: return False # other wise, you need to be 1 byte, which first bit start with 0. 
                
            else:
                if (num & 0xC0) != 0x80: return False
                count -= 1
            
        return count == 0


def validUtf8_2(self, data: List[int]) -> bool:
    
    # the UTF8 is at most 4 bytes long
    # so the first bit is at most 4 1
    
    count = 0 # count # of byte remaining
    
    for num in data:
        
        if count == 0:
            
            if bin(num >> 5)   == '0b110'  : count = 1
            elif bin(num >> 4) == '0b1110' : count = 2
            elif bin(num >> 3) == '0b11110': count = 3
            elif bin(num >> 7)  == '0b1': return False # other wise, you need to be 1 byte, which first bit start with 0. 
            
        else:
            if bin(num >> 6) != '0b10': return False
            count -= 1
        
    return count == 0

def validUtf8_3(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for c in data:
            if count == 0:
                if (c >> 5) == 0b110:
                    count = 1
                elif (c >> 4) == 0b1110:
                    count = 2
                elif (c >> 3) == 0b11110:
                    count = 3
                elif (c >> 7):
                    return False
            else:
                if (c >> 6) != 0b10:
                    return False
                count -= 1
        return count == 0