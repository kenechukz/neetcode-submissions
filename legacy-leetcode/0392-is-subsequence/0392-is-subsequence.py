class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        l,r = 0,0
        count = 0
        if len(s) == 0:
            return True
        while r < len(t):
            if s[l] == t[r]:
                count+= 1
                l+= 1
                r+= 1

            if r == len(t) or l == len(s):
                break

            if t[r] != s[l]:
                r+= 1

            
        return count == len(s)


        