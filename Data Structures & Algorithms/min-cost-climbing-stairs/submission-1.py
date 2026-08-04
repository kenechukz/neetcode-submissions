class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """
        min cost to get past last index
        can start at index 0, or 1
        after cost paid u can move 1 or 2 steps

        [1,2]
        [1, 2]
        start at min index cost (greedy)
        cost = 1
        take 2 steps

        [1, 2, 3]
        
        try greedy
        index = 0
        cost = 1
        2 steps
        index =2
        cost = 4
        take 1 step

        [1,2,1,2,1]
        [-1 ....... ]
        [3,3,2,2,1]
        

        dp: []
        idx 0, min of (1 step and 2 steps)
        
        base case:
            idx >= len(cost)
            return curCost
        min(rec(idx +1, cost ), rec(idx + 2, cost))

        
        """

        memo = [-1] * len(cost)

        def recursion(idx):

            if idx >= len(cost):

                return 0

            memo[idx] = cost[idx] + min(recursion(idx+1), recursion(idx+2))

            return memo[idx]


        return min( recursion(0), recursion(1) )


        


        