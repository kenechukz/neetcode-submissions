class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        from collections import defaultdict, deque

        adj_list = defaultdict(list)

        # base cases:
        wordlistSet = set(wordList)
        if not endWord in wordlistSet or endWord == beginWord:
            return 0

        all_words = wordlistSet.union(set([beginWord, endWord]))
        all_words = list(all_words)

        def valid(w1, w2):
            mismatch = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    mismatch += 1
            return mismatch == 1

        for i in range(len(all_words)):
            for j in range(i + 1, len(all_words)):
                if valid(all_words[i], all_words[j]):
                    adj_list[all_words[i]].append(all_words[j])
                    adj_list[all_words[j]].append(all_words[i])

        def bfs(beginWord, endWord):
            seen = {beginWord}
            q = deque([(beginWord, 1)])

            while q:
                word, steps = q.popleft()

                if word == endWord:
                    return steps

                for nxt in adj_list[word]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))

            return 0

        return bfs(beginWord, endWord)