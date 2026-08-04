class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        R:
        infinite amt of each coin

        return min no. coins needed to make target
        else -1

        E:
        1 <= coins.length <= 10, suggests high time complexity -> backtracking
        1 <= coins[i] <= 2^31 - 1
        0 <= amount <= 10000

        base case:
        cur > amount
        cur == amount

        A:
        [1, 5, 10], amt=12

        [-1, ]


                    1 5 10

                1
            1  5  10
        
        1
        

        """

        coins.sort(reverse=True)
        # [10, 5, 1]


        min_coins = float('inf')
        memo = {}
        def find_min_coin(target, count):
            nonlocal min_coins

            if count >= min_coins:
                return 


            if target == 0:
                min_coins = min(min_coins, count)
                return

            if target in memo and memo[target] <= count:
                return 

            memo[target] = count


            for coin in coins:
                if coin <= target:
                    find_min_coin( target - coin, count + 1)





        find_min_coin(amount, 0) 
        return min_coins if min_coins != float("inf") else -1


        