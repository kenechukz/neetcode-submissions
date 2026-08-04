"""
R:
get and put must be O(1)

get - returns value of key else -1

put - updates value of key if it exists else adds it to cache

if no. keys > capacity, after adding key-value pair to cache
then evict LRU key

capacity =2
1: 1 -> 
1: 1 -> 2: 2 
get(1) -> 1
1: 1 -> 2: 2 -> 1: 1
put(3, 3)
2: 2 -> 3: 3
get(2) -> 2
put(4, 4)
3: 3 -> 4: 4
get(1) -> -1
get(3) -> 3
get(4) -> 4
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node

        # Dummy nodes for least (LRU) and most (MRU) recently used
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least

    # Remove a node from the doubly linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at the MRU (most recent) end
    def _insert(self, node):
        prev, nxt = self.most.prev, self.most
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move this node to MRU end
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # Remove existing node (if it exists) before reinserting
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        # If over capacity, remove LRU node (the one next to 'least')
        if len(self.cache) > self.cap:
            lru = self.least.next
            self._remove(lru)
            del self.cache[lru.key]
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)