from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if not endWord in wordList:
            return 0

        wordList.append(beginWord)
        adj_list = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_list[pattern].append(word)

        res = 1
        seen = set(beginWord)
        queue = deque([beginWord])
        
        print(adj_list)
        while queue:
            for i in range(len(queue)):
                w1 = queue.popleft()

                if w1 == endWord:
                    return res
                for j in range(len(w1)):
                    pattern = w1[:j] + "*" + w1[j+1:]
                    for w2 in adj_list[pattern]:
                        if not w2 in seen:
                            queue.append(w2)
                            seen.add(w2)

            res+=1

        return 0