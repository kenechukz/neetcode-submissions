class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        R:
        upper string s
        k - can choose at most k characters of strings to replace with any other upper

        return longest repeating char
        
        E:
        len s == 1
        k == 0

        constr: k <= s.len
        A:

        s = "AAABABB", k = 1


                "AAABABB"
                 l
                 r
                  rrrrr
                    l

                inc l when l-r+1 - maxf > k

                
        """


        l = 0
        res = maxF = 0
        count = {}
        maxF= 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxF = max(count[s[r]], maxF)
            while (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)

        return res




            


        
        