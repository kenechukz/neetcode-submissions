class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """


          a b c
        a       3
        b       2
        d     1 1  
          3 2 1 0


        if word1[i] == word2[j]:
            cache[i][j] = cache[i+1][j+1]
        """

        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        for j in range(n + 1):
            dp[j] = n - j

        for i in range(m-1, -1, -1):
            nextDp[n] = m - i
            for j in range(n-1, -1, -1):

                if word1[i] == word2[j]:
                    nextDp[j] = dp[j+1]
                else:
                    nextDp[j] = 1 + min(
                        dp[j+1],
                        nextDp[j+1],
                        dp[j])

            dp = nextDp[:]    

        return dp[0]