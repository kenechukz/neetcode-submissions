class Solution:

    def isPrefix(self, cur, pref) -> bool:
        return cur[0:len(pref)] == pref


    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            cur = words[i]
            if self.isPrefix(cur,pref):
                count+=1

        return count
        