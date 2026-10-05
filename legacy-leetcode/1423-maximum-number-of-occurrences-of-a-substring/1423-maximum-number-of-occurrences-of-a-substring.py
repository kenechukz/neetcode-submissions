class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        """
        R:
        inp: s - str
         min <= sub size <= maxSize
         maxLetters -  max no. distinct letters (26)
        return max number of occurences

        E:
        if len s < minSize:
            return 0 
        
        A:
        maxLetters = 2, minSize = 3, maxSize = 4
        s = "aababcaab"
               ^ 
            l to r till =min size reached
            add to map (tmp chang on each loop)
            two for loops
            each iter cnt -  distinct letters
            if cnt > maxLtrs:

            add new letter tro cur sub while < maxSize

            aab
            aba
            bab
            keep track of maxOccurence

        s = "aaba"
         aab
         aba
         aaba
        O(n^2)
          

        map - sub: count 

        aababcaab
        l r
        inc r while < minSize
        
        Optimization:
        we find a substring of size x >= minSize that is valid
        unique chars (x) <= maxLetters
        x = yy
        x - Parent sub string

        => that a substring y of x with length = minSize is also valid
        unique chars (y) <= maxLetters

        since y is less than x, it is contained in x
        we can take a greedy approach
        y occurs twice is x, whereas x occurs once
        """

        maxOcc = 0
        occ = dict()
        n = len(s)

        if n < minSize:
            return 0

        # Find all sub strings
        for i in range(n - minSize +1):
                curSub = s[i:i +minSize]
                if len(set(curSub)) <= maxLetters: 
                    occ[curSub] = occ.get(curSub, 0) + 1
                    maxOcc = max(maxOcc, occ[curSub])

        return maxOcc
                
                
                




        