class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        """
        R: 
        given: 
            int arr (can contain dupl.)
            target
        return:
        all combs. that sum to target

        E:
        nums[0] < target and len(nums) == 1
        curSum == target -> return + add to res
        curSum > tagret or i >= n -> return

        A:

                [9,2,2]
            
        9           
      []  [9]    
         2 
  []  [2]  [9] [9, 2]
                   2     
 [] [2] [2] [2, 2]   [9] [9, 2] [9, 2] [9, 2, 2]

        """


        res = set()
        candidates.sort()
        n = len(candidates)

        def backtracking(i, temp, curSum):
            
            if curSum == target:
                res.add(tuple(temp))
                return 

            if curSum > target or i >= n:
                return


            backtracking(i+1, temp,  curSum)
            backtracking(i+1, temp + [candidates[i]], curSum + candidates[i])
            
        backtracking(0, [], 0)


        return [list(comb) for comb in res]
        