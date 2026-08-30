class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        """
        R:
        given:
            digits: str
        
        digits are between 2-9 inclusive

        return all combinations of digits


        E:
        max str length?
        0 <= digits.length <= 4

        is fg and gf considered duplicates?
        Yes

        base case:
        if digits.length == 0 -> []

        Input: digits = "34"

        Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

                                3 {def} 
(0,"d",0)
                           d            e.    f
                       4 {ghi}
(1, "dg", 1)           g.  h. i    g. h. i  

                        jkl


                              -    3

                                  
        "345"

        "543"

        "d" -> "dg"

        

        """

        res = []
        digits_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        def recurse(curIdx, curStr, depth):
            if depth >= len(digits):
                res.append(curStr)

            for i in range(curIdx+1, len(digits)):
                digit = digits[i]
                for char in digits_map[digit]:
                    recurse(i, curStr + char, depth+1)

            return 
            
        if digits == "":
            return res
        for char in digits_map[digits[0]]:
            recurse(0,char,1)

        return res
        