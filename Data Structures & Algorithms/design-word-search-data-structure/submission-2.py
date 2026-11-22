class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    """

            *

         d    b    m

         a    a    a

         y    y    y
    """

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
    
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, word, start_idx):
            for i in range(start_idx, len(word)):
                ch = word[i]
                if ch in node.children:
                    node = node.children[ch]
                elif ch == ".":
                    for child in node.children:
                        if dfs(node.children[child], word, i+1):
                            return True
                    return False
                else:
                    return False

            return node.is_word

        return dfs(node, word, 0)

        
        
