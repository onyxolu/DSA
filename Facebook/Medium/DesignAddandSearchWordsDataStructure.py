
# Brute force . have a list of words and check for a match
# Optimal is to use a Trie (Prefix Tree) 

class TrieNode:
    def __init__(self):
        self.children = {}  # b: a , up to the 26 characters
        self.word = False # for every xter, want to know if its the end of the word
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:    
        # what do we pass,rem portion of the word to match, index and curNode
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                # Handle .(dot) search
                if c == ".":
                    #e.g .ab
                    for child in cur.children.values():
                        if dfs(i+1, child): # skipping the dot
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)