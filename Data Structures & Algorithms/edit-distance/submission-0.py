class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        R:
        we have 4 choices at each character:
        insert character before
        delete this char
        replace this char
        do nothing

        return min ops to make word1 == word2

        E:
        0 <= word1.length, word2.length <= 100
        word1 and word2 consist of lowercase English letters.
        A:

                    "" m  0
                -        "m"  o  0

                             "mo" n  0

                                "mon"  k  0

                                    "mone" y 1


                                        "money"  "s"  1

                                    "money" "\0" 2


        each state will hold: (idx/curLtr, operation) : noOps

        we want min of each operation at each state
        """

        memo = {}

        def dfs(i, j):
            
            if i >= len(word1) and j >= len(word2):
                return 0

            if i >= len(word1):
                return len(word2) - j

            if j >= len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]


            # cur elems of each word equal
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)

            else:
                
                # otherwise we have 3 choices: replace, delete, insert
                memo[(i, j)] = min(     1 + dfs(i+1, j+1), \
                                                1 + dfs(i+1, j), \
                                                1 + dfs(i, j+1)
                                    )

            
            return memo[(i, j)] 


        return dfs(0, 0)

        
        