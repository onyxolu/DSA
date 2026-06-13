class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, cnt):
        # insert a new sentence
        node = self.root
        for c in word:
            node = node.children[c]
        node.cnt += cnt
    
    def search(self, prefix):
        # return all sentences that match the prefix: list of tuple (sentence, cnt)
        node = self.root
        path = ""
        for c in prefix:
            if c in node.children:
                node = node.children[c]
                path += c
            else:
                return []
        paths = []
        self.all_paths(node, path, paths)
        return paths
    
    def all_paths(self, node, path, paths):
        # return all paths starting from node, paths is list of (str, cnt)
        if node.cnt > 0:
            paths.append((path, node.cnt))
        
        for c in node.children:
            self.all_paths(node.children[c], path+c, paths)
            

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for s, t in zip(sentences, times):
            self.trie.insert(s, t)
        self.current = ""

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.current += c
            tmp = self.trie.search(self.current)
            tmp = sorted(tmp, key=lambda x: (-x[1], x[0]))
            res = [i for i, j in tmp][:3]
        else:
            self.trie.insert(self.current, 1)
            self.current = ""
            res = []
        return res

    