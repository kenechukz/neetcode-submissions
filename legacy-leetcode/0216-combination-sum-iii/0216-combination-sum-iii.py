class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        """
        for i in range(start, min(n+1,10))
        backtracking(1, [], 3, 9)
        backtracking(2, [1], 2, 8) 
        backtracking(3, [1, 2], 1, 6)       ------- 
        backtracking(4, [1, 2, 3], 0, 5) return ^    
        """
        
        def backtracking(start, curRes, k, n):

            if k == 0 and n == 0:
                res.append(curRes)
                return

            if k <= 0:
                return

            for i in range(start, min(n+1, 10)):
                backtracking(i+1, curRes + [i], k-1, n-i)

            return
        backtracking(1, [], k, n) 
        return res   