
from collections import defaultdict, List
# TC = 0(NM), SC = 0(N)

# "acef" -> "bdfg" => "cegh"
# if we are dealing with 0 index, 0245 => 1356 => 2467 => 2578
# We need a hash function to normalize 2578 back to base (0245)
# then store common base in bucket 

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hash(s):
            return tuple([(ord(c) - ord(s[0])) % 26 for c in s])
        groupBy = defaultdict(list)
        for s in strings:
            # print(hash(s))
            # (0, 1, 2)
            # (0, 1, 2)
            # (0, 2, 4, 5)
            # (0, 1, 2)
            # (0, 25)
            # (0, 25)
            # (0,)
            # (0,)

            groupBy[hash(s)].append(s)
        return groupBy.values()
        