
# Hashmap

class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        # dict: set() person to people they prefer over pairs
        d = {} 
        for x,y in pairs:
            d[x] = set(preferences[x][:preferences[x].index(y)])
            d[y] = set(preferences[y][:preferences[y].index(x)])
        # {0: (), 1: (3,2), 2: (), 3: (1,2)}  
        result = 0
        for x in d:
            for y in d[x]:
                if x in d[y]: # u prefers x over y
                    result += 1
                    break
        return result