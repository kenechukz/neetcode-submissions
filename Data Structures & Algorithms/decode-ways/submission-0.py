class Solution:
    def numDecodings(self, s: str) -> int:

        """
        R:
        Given string s (of digits)

        return no of ways to decode it
        E:
        1 <= s.length <= 100
        s consists of digits

        if len(s) ==  1 -> 1
        A:

        if no. numbers in grouping > 26:
            don't count that grouping

        if any number has leading zero in grouping:
            don't count that grouping


        1 2 1


            1     12
        2    21    1
       1
        """

        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456") ):

                res += dfs(i+2)

            dp[i] = res

            return res

        return dfs(0)




        
