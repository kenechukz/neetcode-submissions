class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        given prices, prices[i] is price on ith day

        rules for buying and selling:
        after selling you can't buy for on the next day
        you can only own one NeetCoin at a time

        return max profit

        E:
        if len of prices == 1 -> 0
        1 <= prices.length <= 5000
        0 <= prices[i] <= 1000

        A:
        prices = [1,3,4,0,4]
         buy on day 0 (price = 1)
         sell on day 1 (price = 3) 3-1 = 2 profit
         buy on day 3 (price = 0)
         selling on day 4 (price = 4) 4 - 0 = 4 profit

        total profit 2 + 4 = 6


        """

        # if buying -> i + 1
        # if selling -> i + 2

        # stores: (i, buying) : max_profit
        dp = {}

        # buying is a boolean
        def buy_sell_cooldown(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = buy_sell_cooldown(i+1, buying)
            if buying:
                buy = buy_sell_cooldown(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = buy_sell_cooldown(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)


            return dp[(i, buying)]

        return buy_sell_cooldown(0, True)