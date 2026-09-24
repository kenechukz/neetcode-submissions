class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        R:
        
        given:
            s: str
            p: str

        . -> match any single char
        * -> match zero or more preceding elements

        return true if pattern p matches input string


        E:

        can we compound . and *? Yes

        Input: s = "xyz", p = ".*z"
        Output: true

        "Each appearance of '*', will be preceded by a valid character or '.'."
        1 <= s.length <= 20
        1 <= p.length <= 20

        base case:

            if no other methods matched:
                return false

        A:

        Input: s = "xxxyz", p = ".*z"

        Output: true

                xxxxyz         .*z
                i              j       prev_elem = ""

                 i              j



        match 0.                    match n

xxxxyz  .*z                        xxxxyz  .*z   
 i        j                          i      j


when we have a *, each recursive call can continue n times or 0 times
            
            we only proceed i if we can match

            if p[j]== "*" and cur_elem == prev_elem or prev_elem == ".":
                

            if p[j] == ".":
                we must match char
                prev_elem = "."






        example:
        """

        n, m = len(s), len(p)
        dp = [[None] * (m + 1) for _ in range(n + 1)]

        def func(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            if j == m:
                res = i == n
            else:
                head_match = i < n and (p[j] == s[i] or p[j] == ".")

                """
                Handles case: 
                    s="aab"
                    p="c*a*b"
                    Output: true
                """
                if j + 1 < m and p[j + 1] == "*":
                    # skip the x* pair, or consume one char and stay on it
                    res = func(i, j + 2) or (head_match and func(i + 1, j))
                else:
                    # if head_match is False, it short circuits
                    res = head_match and func(i + 1, j + 1)

            dp[i][j] = res
            return res

        return func(0, 0)


        