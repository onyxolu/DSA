# The idea behind this is to use KMP string matching, this is a classic single string matching algo. The trick here is that we search the KMP list multiple times to see if increasing A will help us find an answer.

# for example:
# A = "abcd"
# B = "cdabcdab"

# A can only fit into B a maxmimum of two times evenly.
# ceiling = 2 ((len(B) - 1) // len(A) + 1 , how many times A fits in B)

# search A * 2, can B fit in A?

# (A * 2) = abcdabcd
# B = cdabcdab

# search A * 2, now can B fit in A?

# (A * 3) = abcdabcdabcd
# B = cdabcdab

# This does work! We can return 3, because A * 3 (abcdabcdabcd ) does produce a valid solution, original B string between the brackets ( ab{cdabcdab}cd )

# If neither of these are true, we can bail out. This is because once we have gone x3 the original string, we will never get an answer, as duplicating A any more times will not help produce an answer.

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = (len(B) - 1) // len(A) + 1  # Ceiling.
        kmp = self.kmpTable(B)  # build kmp pattern table

        for i in range(0, 2):
            index = self.search(kmp, A * (times + i), B)

            if index is not None:
                return times + i

        return -1

    def search(self, kmp, str, pattern):
        j = 0  # num of patterns match in pattern (string B)

        for i in range(len(str)):
            while j > 0 and str[i] != pattern[j]:
                j = kmp[j - 1]  # fall back to best known match in our kmp list

            if str[i] == pattern[j]:
                j += 1

                if j == len(pattern):
                    return i - (j - 1)

        return None

    def kmpTable(self, s: str):
        kmp = [0] * len(s)

        for i in range(1, len(s)):
            idx = kmp[i - 1]

            while idx > 0 and s[idx] != s[i]:
                idx = kmp[idx - 1]  # trace backwards to find the last matching char

            if s[i] == s[idx]:  # matches next char, increment our last known good case
                idx += 1

            kmp[i] = idx

        return kmp

# In this problem, you have to consider the worse case scenario, really actively try to create the worse case scenario. The 3 is there for the worst case scenario because of the rounding down from int, the fact that range(N) only takes you to an index of N-1 and to cover the situation where there is an extra letter at the front and the back of B.

# Consider A = 'abc' and B = 'abcabcabc': len(B)/len(A) = 3. However, you cannot do range(1,3), you will need range(1,4). So this causes us to need at the minimum int(len(B)/len(A)) + 1
# Consider A = 'abc' and B = 'abcabcab': Now you get int(len(B)/len(A)) = 2 and we will still need range(1,4) so it will be int(len(B)/len(A)) + 2 because it rounded down. So we will need at least +2 to be safe so far.
# Finally, consider the worst case scenario A = 'abc' and B = 'cabcabca': In this case we will need to buffer in front and at the end because of how the string starts and ends (starts with c and ends with a). We get int(len(B)/len(A)) = 2. However we will need 4 copies of A to cover B: ab[cabcabca]bc. This means we need range(1,5) which means we will need int(len(B)/len(A)) + 3. This is definitely the worst case scenario because aside from the start and finish of B both needing extra copies, the rounding down, and the range(N) only going up to N-1 there is no other way to create a worse situation.

def repeatedStringMatch(self, A: str, B: str) -> int:
    	if set(B).issubset(set(A)) == False: return -1
    	for i in range(1,int(len(B)/len(A))+3):
    		if B in A*i: return i
    	return -1