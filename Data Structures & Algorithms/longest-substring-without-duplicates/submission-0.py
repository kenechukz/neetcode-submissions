class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        R:
        return longest substring without dupl. chars
        E:

        if len s == 0 or 1:
            return

        A:

        "zxyzxyz"

         l
        r 

        increment r while s[r] != s[l]

        if s[l] == s[r]:
            increment l while s[l]not equal to s[r]

        check max length on each iter if valid substring

        """

        charSet = set()
        l = 0
        maxSub = 0

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l+= 1

            charSet.add(s[r])
            maxSub =  max(maxSub, r-l + 1)

        return maxSub

        