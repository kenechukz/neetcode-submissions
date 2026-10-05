class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if len(word1) > len(word2):
            biggerStr = word1
            smallerStr = word2
        else:
            biggerStr = word2
            smallerStr = word1

        newStr = []
        i = 0

        while i < len(smallerStr):
            newStr.append(word1[i])
            newStr.append(word2[i])
            i+=1

        while i < len(biggerStr):
            newStr.append(biggerStr[i])
            i+=1

        return ''.join(newStr)

        


        
