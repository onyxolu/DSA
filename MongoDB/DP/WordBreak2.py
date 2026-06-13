class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        cache = {}

        def backtrack(index):
            if index == len(s):
                return [""]
            if index in cache:
                return cache[index]

            res = []
            curr = trie.root
            for i in range(index, len(s)):
                char = s[i]
                if char not in curr.children:
                    break
                curr = curr.children[char]
                if curr.isWord:
                    for suffix in backtrack(i + 1):
                        if suffix:
                            res.append(s[index:i + 1] + " " + suffix)
                        else:
                            res.append(s[index:i + 1])

            cache[index] = res
            return res

        return backtrack(0)