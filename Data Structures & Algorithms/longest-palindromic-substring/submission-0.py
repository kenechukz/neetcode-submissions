class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
        R:
        given string s

        return longest substr of s that is palindrome

        if tie, return either

        E:  
        1 <= s.length <= 1000
        s contains only digits and English letters.
        

        if tie, return either
        A:

        worst case: O(N^2)
        "ababd"

        "baac"

        []

        ["a", "b", "a", "b", "d"]

        "a", "ab", "aba", "abab", "ababd" 

        ["a","a",]
        """     
        n = len(s)
        maxSub =[None] * n

        for i in range(n):
            curSub = ""
            curMax = [] 
            for j in range(i, n):
                curSub += s[j]
                if curSub == curSub[-1::-1]:
                    curMax = [curSub, j - i + 1]
                    

            if i > 0:
                #print(maxSub[i][1], maxSub[i-1][1])
                if curMax[1] >= maxSub[i-1][1]:
                    maxSub[i] = curMax
                else:
                    maxSub[i] = maxSub[i-1]
            else:
                maxSub[i] = curMax

        return maxSub[-1][0]




                


                





        