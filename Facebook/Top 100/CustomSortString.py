from collections import defaultdict, Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lk = defaultdict(int)
        i = 0
        for c in order:
            lk[c] = i
            i+=1
            
        return "".join(sorted(s, key=lambda x:lk[x]))
            
        
class Solution(object):
    def customSortString(self, S, T):
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = Counter(T)
        ans = []
        print(count)

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0
        print(ans)
        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)