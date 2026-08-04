class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        """
        Longest Common Subsequence — Dynamic Programming Approach

        Steps:
        1. Create a 2D DP table where dp[i][j] represents the LCS length
        of text1[i:] and text2[j:].

        2. Fill the table bottom-up, starting from the end of both strings.

        3. For each position (i, j):
        - If characters match (text1[i] == text2[j]):
                dp[i][j] = 1 + dp[i+1][j+1]
            (there reason we add 1 to diagonal, is because the diagonal represents suffix of
             this current LCS we are creating, and since we have matched another character we
             have now added another character to this suffix of matching characters)

        - If they do NOT match:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
            (skip a character from either string and choose the best)

        4. The answer is dp[0][0], meaning the LCS length for both full strings.

        Why this works:
        - Matching characters “lock in” 1 and move diagonally (i+1, j+1).
        - Non-matching characters branch into two subproblems, and we choose the larger.
        - Every subproblem reuses results stored in dp, avoiding exponential recursion.
        """

        n, m = len(text1), len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]



        