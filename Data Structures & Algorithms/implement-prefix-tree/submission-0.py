
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.children.get(ch):
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_word = True

    def _find(self, word):
        curr = self.root
        for ch in word:
            if not curr.children.get(ch):
                return None
            curr = curr.children[ch]
        
        return curr

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_word


        

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        
        