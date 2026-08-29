class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        """
        R:
        given:
            nums: arr[int]

        return true if for some s1 and s2, sum(s1) == sum(s2)
        else false

        E:
        what's max len of arr
        1 <= nums.length <= 100
        what's max val of nums[i]
        1 <= nums[i] <= 50

        ** Potentially higher time complexity?

        A:

        sub sets must contain all nums in list

        nums = [1,2,3,4]
        sum(nums) = 10
        Output: true

        nums = [1,2,3,4,5]
        sum(15)
        Output: false

        precondition: 
        if sum(nums) % 2 != 0:
            return False

        each subset needs to sum to sum(nums)/2


        [1,2,3,4]

        goal: 5

                    1
                2.  3.  4


                [1, 4]

                2
            3
             

        [1,2,3,4,5,7]



        sum(nums) = 22

        goal: 11

                    7

            1   2.  3.  4.  5
                        
                [7,4] = 11

            [1, 2, 3, 5] = 11


        (12, 14, 16) = 42

        we need 21


               sum(nums) = 22

        goal: 11

                    1

           2.  3.  4.  5.  7

           3 4 5 7


           457

        7 11

        dp[i] = 



        base case:
            if curNum == goal:


        def func:

            if curSum + newNum == goal?
             return True

            if not currSum + newNum > goal
                continue
        """


        nums.sort(reverse=True)
        visited = set()
        visited.add(0)




        if sum(nums) % 2 != 0:
            return False

        goal = sum(nums) / 2 

        if goal in nums:
            return True

        def backtrack(curSum, depth):
            if curSum == goal:
                return True

            if depth >= len(nums) or curSum > goal:
                return False
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                if backtrack(curSum + nums[i], depth + 1):
                    return True
                visited.remove(i)
            return False

        if backtrack(nums[0], 0):
            return True
        return False
        
        
        
         


        