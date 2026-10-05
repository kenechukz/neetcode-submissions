class Solution:
    def letterCombinations(self, digits: str) -> List[str]:



        """
        input: 23

                     2
            a        b         c
          d e f   d  e  f    d e f

        """

        hashMap = { '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                }
        res = []
        n = len(digits)
        if digits == "":
            return res

        def backtracking(i, curRes):
            if len(curRes) == n:
                res.append(curRes)
                return

            for ch in hashMap[digits[i]]:
                backtracking(i+1, curRes + ch)



        backtracking(0, "")

        return res
