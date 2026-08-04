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

        m = len(word1)
        n = len(word2)

        
        cache = [[float("inf")] *  (n + 1) for i in range(m + 1)]  

        for j in range(n, -1, -1):
            cache[m][j] = n - j

        for i in range(m, -1, -1):
            cache[i][n] = m - i

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i+1][j+1],
                        cache[i][j+1],
                        cache[i+1][j])

        print(cache)
        return cache[0][0]