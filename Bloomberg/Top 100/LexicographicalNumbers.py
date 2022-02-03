

# Step1: Converting every number in [1, n] to a string and building a Trie. Treat each number as a word.
# Step2: Running DFS to save every words in the Trie and converting them back to number.

# Time:O(N)
# Space:O(N)

class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        

class Solution:
    
    def __init__(self):
        self.trie_root = TrieNode()
        self.result_list = []
    
    def build_trie(self, s):
        
        c_node = self.trie_root
        for c in s:
            if(c not in c_node.children):
                c_node.children[c] = TrieNode()
            c_node = c_node.children[c]
            
        c_node.is_end = True
        
    def print_trie(self, c_node, cs):
        
        if(c_node.is_end):
            self.result_list.append(int(cs))
        
        for c, n_node in c_node.children.items():
            self.print_trie(n_node, cs+c)
        
        return
    
    
    
    def lexicalOrder(self, n: int):
        
        for i in range(1, n+1):   
            s = str(i)
            self.build_trie(s)
        
        self.print_trie(self.trie_root, '')
        
        return self.result_list








# Basice idea: think about Trie. we append digits to the specific suffix until we reach the target number.

class Solution:
    def lexicalOrder(self, n: int):
        # recursively use Trie
        res = []
        if n < 10:
            return list(range(1, n+1))
        for i in range(1, 10):
            res += [i]
            res += self.helper(i, n)
        return res
    
    def helper(self, start, n):
        res = []
        for aux in range(10):
            newStart = start*10+aux
            if newStart > n:
                break
            res += [newStart]
            res += self.helper(newStart, n)
        return res