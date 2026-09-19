class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        """
        R:
        given:
            s: str
            t: str

        return no. distinct subsequences of s equal to t

        subsequence meaning characters must come one after the other

        E:
        will len(s) always be >= len(t)? -> we can add a check for this

        1 <= s.length, t.length <= 1000

        Always lowercase ? -> leave as is so we match based on case

        time complexity: O(s * t) worst case

        Each subsequence needs to be of length(t)

        A:

        dp[i][j]

        Input: s = "xxyxy", t = "xy"

        we start from left going right, two pointers i and j

        f(0, 0)  take

        skip ---
         |
         |

        """




        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]


        def validWay(i, j):

            # We got a hit since t is exhausted
            if j == len(t):
                return 1

            # No hit since s is exhausted and t is not
            if i == len(s):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            # We take if we get a match   

            ways = validWay(i+1, j)
            if s[i] == t[j]:
                ways+=validWay(i+1, j+1)

            dp[i][j] = ways

            return dp[i][j]

        return validWay(0,0)


        
