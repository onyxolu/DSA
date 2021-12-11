
class Solution:
    def isNumber(self, s: str) -> bool:
        # ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
        digit, dec, e, symbol = False, False, False, False
        
        for c in s:
            # digits
            if c in "0123456789":
                digit = True
            # symbols
            elif c in "+-":
                if symbol or digit or dec:
                    return False
                else:
                    symbol = True
            # exponent
            elif c in "Ee":
                if not digit or e: return False
                else:
                    e = True
                    symbol = False
                    digit = False
                    dec = False
            # decimal
            elif c == ".":
                if dec or e: return False
                else:
                    dec = True
            else:
                return False
            
        return digit
        
        
        
# float => Cheating

# class Solution:
#     def isNumber(self, s: str) -> bool:
#         if s.lower().startswith(('inf', '+inf', '-inf')):
#             return False
        
#         try:
#             float(s)
#             return True
#         except Exception:
#             return False