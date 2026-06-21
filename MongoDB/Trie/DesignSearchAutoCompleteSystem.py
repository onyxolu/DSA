import collections
from typing import List

# Clarify: top 3 by frequency? ties broken by ASCII? # resets input and stores sentence?
# Key insight: Trie for prefix search + DFS to collect all sentences under prefix
# Building on Implement Trie — same structure, add frequency count per node
#
# Volunteer before being asked:
#   - defaultdict(TrieNode) → cleaner than manual if c not in children
#   - DFS from prefix node → collect all complete sentences under that prefix
#   - Sort key (-freq, sentence) → handles both frequency and ASCII tiebreaker
#   - current buffer tracks typed input, reset on #
#   - Real world: Google search suggestions, IDE autocomplete, mobile keyboard prediction

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)  # char → TrieNode
        self.cnt = 0                                        # frequency of complete sentence

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, cnt: int) -> None:
        node = self.root
        for c in word:
            node = node.children[c]                        # auto-creates node if missing
        node.cnt += cnt                                    # increment frequency

    def search(self, prefix: str) -> List[tuple]:
        node = self.root
        path = ""

        # traverse to end of prefix
        for c in prefix:
            if c not in node.children:
                return []                                   # prefix not found
            node = node.children[c]
            path += c

        # DFS to collect all sentences under prefix node
        paths = []
        self._dfs(node, path, paths)
        return paths

    def _dfs(self, node: TrieNode, path: str, paths: List[tuple]) -> None:
        if node.cnt > 0:
            paths.append((path, node.cnt))                 # complete sentence found
        for c in node.children:
            self._dfs(node.children[c], path + c, paths)  # explore all children


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for s, t in zip(sentences, times):
            self.trie.insert(s, t)
        self.current = ""                                  # current typed input buffer

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.current += c
            results = self.trie.search(self.current)
            results = sorted(results, key=lambda x: (-x[1], x[0]))  # -freq, ASCII
            return [sentence for sentence, _ in results][:3]         # top 3
        else:
            self.trie.insert(self.current, 1)              # store new sentence
            self.current = ""                              # reset buffer
            return []

# Edge cases:
#   prefix not in trie → search returns [] → input returns []
#   # after single char → stores single char as sentence
#   same sentence typed again → frequency increments by 1
#   tie in frequency → ASCII order decides (sorted handles this naturally)

# Complexity:
#   __init__ → O(n × m) where n = sentences, m = avg length
#   input    → O(p + s log s) where p = prefix length, s = matching sentences
#   space    → O(n × m) for trie + O(s) for DFS results

# Follow-ups:
#   Top k instead of top 3 → change slice [:3] to [:k]
#   Thread safe → threading.Lock on insert and search
#   Large dataset → store top 3 at each Trie node to avoid DFS + sort on every input
#   Distributed → shard by first character, merge results from shards
#   Real world: Google Suggest, IDE autocomplete, mobile keyboard prediction