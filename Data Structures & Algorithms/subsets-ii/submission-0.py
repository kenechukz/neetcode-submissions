class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        """
        R:
        given: nums - int
        return all subsets (can contain duplicate elems in nums)


                    [1 2 1]

                 []                     1 
                            [1 2]    
                []   1              1       1,1
                              [2]
            []  [2] [1] [1,2]    [1]  [1,2]  [1,1] [1,1,2]
              
        E: 
         depth >= n
        """
        nums.sort()
        n = len(nums)
        res = []



        def backtracking(i, curRes):

            if i >= n:
                res.append(tuple(curRes))
                return

            backtracking(i+1, curRes)
            backtracking(i+1, curRes + [nums[i]])



        backtracking(0, [])
        res = set(res)
        res = [list(x) for x in res]
        return res


        