
# Hashmap

def roman2Int(s):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and dict[s[i+1]] > dict[s[i]]:
            result -= dict[s[i]]
        else: result += dict[s[i]]

    return result


print(roman2Int("MCMXCIV"))