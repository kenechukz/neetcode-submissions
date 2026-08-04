
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)



        def backtracking(i, temp, curSum):

                if curSum == target:
                    res.append(temp)
                    return 
                    
                if curSum > target or i >= n:
                    return

                backtracking(i, temp + [nums[i]], curSum+nums[i])
                backtracking(i+1, temp , curSum)

        backtracking(0, [], 0)

        return res
        