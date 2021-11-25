
# Edge cases

from typing_extensions import IntVar


# IV - 4
# IX - 9
# XL - 40
# XC - 90
# CD - 400
# CM - 900

def intToRoman(num):
    symbolLIst = [["I", 1], ["IV", 4], ["V",5], ["IX", 9], 
                    ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                    ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                    ["M", 1000]]
    # We use list instead of hashmap to keep the correct order
    res = ""
    for sym, val in reversed(symbolLIst):
        if num // val:
            count = num // val
            res += (sym * count)
            num %= val

    return res

