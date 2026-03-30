import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char] 
        
        current.eow = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            current = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for children in current.children.values():
                        if dfs(i + 1, children):
                            return True
                    return False
                if char not in current.children:
                    return False
                current = current.children[char] 
            
            return current.eow
        
        return dfs(0, self.root)

        
