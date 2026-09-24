class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        """
        A:

        s="aab"
        p="c*a*b"
        Output: true

            aab         c*a*b
            i           j

                2 options if p[j] == "*":
        skip (i, j+2)               consumer char only if head matches (i+1, j) 
                else:
                    we match chars and check remained of string only if head_match

                    res = head_match and func(i+1, j+1)

    aab.   c*a*b        aab             c*a*b
     i.      j           i

        we try head match, 
        
        head_match = s[i] == p[j] or p[j] == "."

        we check if pattern is exhausted:  if j == m -> res = i == n

        else 

        we enter recusive body:

            we check: if p[j] == * ? -> skip or consume one char
        """

        n,m = len(s), len(p)
        dp = [[None] * (m+1) for _ in range(n+1)]


        def func(i,j):

            
            if dp[i][j] != None:
                return dp[i][j]

            if j == m:
                res = i == n

            else:
                head_match = i < n and (s[i] == p[j] or p[j] == ".")

                if j + 1 < m and p[j+1] == "*":
                    # skip or match
                    res = func(i, j+2) or (head_match and func(i+1, j))

                else:
                    res = head_match and func(i+1, j+1)

            dp[i][j] = res
            return res

        return func(0,0)






        