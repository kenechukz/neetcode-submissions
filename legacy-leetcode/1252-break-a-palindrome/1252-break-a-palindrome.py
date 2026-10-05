from collections import Counter
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        """
        R:
        lowercase palin
        repl. exactly 1 char
        make lexi smallest

        "abcc" < "abcd"
        
        if non exists return ""

        E:
        if len == 1:
            return palindrome

        if palin ==  "bbbb"
        A:
        "abccba"

        abba

        find divider of palindrome (half of length of string)

        aba
        
        wobow
        """
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''



            

            
        