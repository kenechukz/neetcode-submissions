class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        R:

        given: prices, ith price is price on ith day
        return max profit


        E:
        length of prices == 1 -> return 0


        A:
        [10, 1, 5, 6, 7, 1]
             l       
                      r

        if price[l] > price[r]:
            l = r
            r++

        """
        maxProf = 0
        l,r = 0,1

        while l<= r and r < len(prices):

            if prices[l] > prices[r]:
                l = r
                r+= 1

            else:
                maxProf = max(maxProf, prices[r] - prices[l])
                r+= 1

        return maxProf
