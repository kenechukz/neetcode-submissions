class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        given
        s1, s2, s3

        return true if s3 is formed by interleaving s1 and s2 else false

        to interleave:
        s1 and s2 are divided into substrings n and m respectively

        len(n-m) <= 1
        Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

        E:
        lowercase english letters


        A:

        s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"


        at each stage we can pick a char from s1 or s2

        "aabbbbaa"

                    ""
            s1: "a"              s2: "b"
        (i:1)     (i:0)
        s1:"a"      s2:"b"
      (i:2)   (i:0)
      s1: "a" s2:"b"
            (i:2)   (i:1)
            s1: "a" s2:"b"

        """
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(i,j,k):
            if k >= len(s3):
                return abs(j-i) <= 1
            cur = s3[k]

            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if i < len(s1) and j < len(s2):
                if s1[i] == cur and s2[j] == cur:
                    memo[(i+1, j, k+1)] = dfs(i+1, j, k+1) 
                    memo[(i, j+1, k+1)] = dfs(i, j+1, k+1)

                    return memo[(i+1, j, k+1)] or memo[(i, j+1, k+1)]
                elif s1[i] == cur:
                    memo[(i+1, j, k+1)] = dfs(i+1, j, k+1)
                    return memo[(i+1, j, k+1)]
                elif s2[j] == cur:
                    memo[(i, j+1, k+1)] = dfs(i, j+1, k+1)
                    return memo[(i, j+1, k+1)]
                else:
                    return False
            else:
                if i < len(s1) and s1[i] == cur:
                    memo[(i+1, j, k+1)] = dfs(i+1, j, k+1)
                    return memo[(i+1, j, k+1)]

                elif j < len(s2) and s2[j] == cur:
                    memo[(i, j+1, k+1)] = dfs(i, j+1, k+1)
                    return memo[(i, j+1, k+1)]

            return False

        return dfs(0,0,0)



        # at the end we subtract index of s1 and s2

        