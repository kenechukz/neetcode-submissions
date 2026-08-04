class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        given nums: int[]
        target: int

        return no. ways to build expression s.t. sum = target

        E:
        1 <= nums.length <= 20
        0 <= nums[i] <= 1000
        -1000 <= target <= 1000

        A:
        [2,2,2], target = 2

        +2 +2 -2
        we have 2 possible ways to arange + 2
        we have 1 way to arrange -2

        nums=[1,1] target = 0
        nums[1, 2] target = -1  

                []
            -1     +1

          -2  +2  -2 +2
          -3  1   -1  3


        dp(i, sum)
        cur 






        For each number in the array, you can choose to either add or subtract it to a total sum.


        traverse starting at each nums[i] (two for loops)

        [2,2,2]

        everytime our decision is whether we add or sub


                []

            -2         +2

        -2     +2    -2    +2

       -2 +2  -2 +2  -2 +2  -2 +2

       -6 -2  -2 +2  -2 +2  +2  +6 
       
       
        memo = []
        dp(i+1, sum + nums[i])
        dp(i+1, sum - nums[i])

        memo[dp(i, sum)] = result

        """

        memo = {}
        def dp(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = dp(i+1, cur_sum + nums[i]) + dp(i+1, cur_sum - nums[i])

            return memo[(i, cur_sum)]

        return dp(0, 0)
        