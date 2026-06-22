from typing import List

# ─── Word Break — O(n² × m) time | O(n) space, m = avg word length ───
# Clarify: case sensitive? words can repeat? empty string valid?
# Key insight: dp[i] = "can s[i:] be segmented?" — work backwards from end
# dp[n] = True is the base case (empty remainder is always valid)
#
# Volunteer before being asked:
#   - Could also use a Trie for word lookup if wordDict is large → faster substring matching
#   - Top-down memoization is equivalent, this is bottom-up tabulation
#   - Real world: text tokenization, search query segmentation (e.g. "newyorktimes" → "new york times")

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True                                # empty string is always valid

        for start_index in range(n - 1, -1, -1):
            for word in wordDict:
                end_index = start_index + len(word)
                if end_index <= n and s[start_index:end_index] == word:
                    dp[start_index] = dp[end_index]
                if dp[start_index]:
                    break                            # found a valid segmentation, stop early

        return dp[0]

# Edge cases:
#   s is empty → dp[0] relies on dp[0]==dp[n]==True trivially
#   no valid segmentation → dp[0] stays False
#   word longer than remaining s → end_index > n, skipped by bounds check

# Complexity:
#   time  → O(n × m × k) — n positions, m words, k = avg word length for slicing/comparison
#   space → O(n) for dp array

# Follow-ups:
#   wordDict is huge → convert to a set for O(1) average lookup instead of list iteration
#   Want actual segmentation, not just True/False → see Word Break II below


# ─── Word Break II — O(2^n) worst case time | O(2^n) space ───
# Returns ALL possible sentences, not just whether one exists
# Key insight: same dp foundation, but build up list of valid sentences instead of boolean
# Use memoization to avoid recomputing the same suffix multiple times

class SolutionII:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)                     # O(1) lookup
        memo = {}                                    # cache: start_index → list of valid sentences

        def backtrack(start_index: int) -> List[str]:
            if start_index == len(s):
                return [""]                          # base case: empty suffix → one empty sentence

            if start_index in memo:
                return memo[start_index]             # avoid recomputing same suffix

            sentences = []
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in wordSet:
                    # recursively get all ways to complete the rest of the string
                    for rest in backtrack(end_index):
                        sentences.append(word + ("" if rest == "" else " " + rest))

            memo[start_index] = sentences
            return sentences

        return backtrack(0)

# Edge cases:
#   no valid segmentation at all → returns []
#   entire string is one word → returns [s]
#   multiple valid segmentations → returns all of them, order not guaranteed

# Complexity:
#   time  → O(2^n) worst case (exponential possible segmentations), memoization helps but doesn't
#           change worst case since output itself can be exponential
#   space → O(2^n) to store all sentences in worst case

# Follow-ups:
#   Why memoize on start_index only, not (start_index, path so far)? → because the SET of valid
#     completions for "rest of string from index i" never changes regardless of prefix
#   wordDict very large → convert to Trie for faster prefix matching during the inner loop
#   Just need count of segmentations, not the strings → simpler O(n²) DP, just count not concat