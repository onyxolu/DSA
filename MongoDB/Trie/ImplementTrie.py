# Clarify: lowercase only? empty strings possible? duplicate inserts?
# Key insight: each node has children map + endOfWord flag
# endOfWord distinguishes complete word from prefix
#
# Volunteer before being asked:
#   - children as dict → O(1) lookup, flexible (vs array of 26 → O(1) but more space)
#   - _traverse helper → eliminates repeated traversal logic in search and startsWith
#   - Real world: autocomplete, spell checkers, IP routing tables, DNA sequencing

class TrieNode:
    def __init__(self):
        self.children = {}                                 # char → TrieNode
        self.endOfWord = False                             # marks complete word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _traverse(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None                               # character missing
            cur = cur.children[c]
        return cur                                        # return final node

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()              # create node if missing
            cur = cur.children[c]
        cur.endOfWord = True                              # mark end of word

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.endOfWord        # must be complete word

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None         # prefix exists, endOfWord irrelevant

# Edge cases:
#   search prefix → returns False (endOfWord=False)
#   startsWith complete word → returns True
#   duplicate insert → idempotent, endOfWord already True
#   single character word → root → node, endOfWord=True

# Complexity:
#   insert     → O(m) where m = word length
#   search     → O(m)
#   startsWith → O(m)
#   space      → O(n × m) where n = number of words, m = average word length

# Follow-ups:
#   Delete word → unmark endOfWord, clean up orphan nodes
#   Count words with prefix → store count at each node, increment on insert
#   Thread safe → threading.Lock on insert
#   Wildcard search (. matches any) → recursive DFS at each . character
#   Real world: autocomplete (next problem!), spell checker, IP routing (longest prefix match)