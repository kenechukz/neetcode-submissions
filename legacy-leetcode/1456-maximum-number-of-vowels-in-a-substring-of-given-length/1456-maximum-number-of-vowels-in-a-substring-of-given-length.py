class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        l=0
        r=k-1
        maxVowels = 0
        vowelCount = 0
        for i in range(k):
            if s[i] in vowels:
                vowelCount += 1
        l+=1
        r+=1
        maxVowels = vowelCount
        while r < len(s):
            if s[l-1] in vowels:
                vowelCount-=1
            if s[r] in vowels:
                vowelCount+=1
            if vowelCount > maxVowels:
                maxVowels = vowelCount
            l+=1
            r+=1

        return maxVowels

                


            




            
        