class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        R:
        given s: string, wordDict: List[str]

        return True if s can be segmented in words containing dict

        can reuse words in dict
        all dict words unique

        E:
        1 <= s.length <= 200
        1 <= wordDict.length <= 100
        1 <= wordDict[i].length <= 20

        if the max len word in wordDict has len > s -> false
        A:
        s = "applepenapple", wordDict = ["apple","pen","ape"]



        """
        n = len(s)
        dp = [False] * (n + 1)

        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:

                if (i + len(word)) <= len(s) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]

        

                     
            
        
        