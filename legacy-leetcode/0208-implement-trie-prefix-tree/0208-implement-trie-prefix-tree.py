class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:

    """
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True

    trie.insert("apple")        ->      (root)
                                    a
                                p
                            p
                        l
                    e (end)

    trie.insert("api")   ->             (root)
                                    a
                                p
                            p      i (end)
                        l
                    e (end)

    trie.insert("pizza")   ->             (root)
                                    a         p
                                p                 i
                            p      i (end)          z
                        l                               z
                    e (end)                                 a (end)

    good resource to understand tries: https://www.youtube.com/watch?v=oobqoCJlHA0

    """

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if not ch in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True
                
        

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if not ch in cur.children:
                return False
            cur = cur.children[ch]

        return cur.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if not ch in cur.children:
                return False
            cur = cur.children[ch]

        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)