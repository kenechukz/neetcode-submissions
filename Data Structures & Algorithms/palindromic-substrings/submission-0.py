class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        R:
        given string s

        return no. of substrs within s that are paliindrome
        E:
        1 <= s.length <= 1000
        s consists of lowercase English letters.


        A:
        s = "aaa"

        i = 0
        "a", "aa", "aaa"
        i = 1
        "a", "aa"
        i = 2
        "a"
        """


        no_palindromes = 0
        n = len(s)

        for i in range(n):
            curSub = ""
            for j in range(i, n):
                curSub += s[j] 
                if curSub == curSub[-1::-1]:
                    no_palindromes +=1

        return no_palindromes
        
        
        
        