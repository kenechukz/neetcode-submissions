class Solution:
    """
    R:
    We are counting distinct ways to sum up to amount with unlimited coins

    state:
    Let dp[i] = num of ways to sum to i with coins

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3 (1+1+1, 1+2, 3)
    dp[4] = 4


                

    A:
    Input: amount = 4, coins = [1,2,3]

    Output: 4

    1 + 1 + 1 + 1 = 4
    2 + 2 = 4
    1 + 3 = 4
    1 + 1 + 2 = 4


                dp[4]

        dp[1]  dp[2]   dp[3]
            
            1     1 + 1    1



                dp[3]

            dp[2]     dp[1]
            1+1       1
            2



    amount = 7, coins = [2,4]
    
    if 7 % 4 exists or == 0
    if 7 % 2 exists == 0

                        dp[7]

                    dp[2]      dp[4]



    amount = 8, coins = [2,4]


                dp[8]   

                dp[2]    dp[4]
                    
                dp[2]
                    1      dp[4]  dp[2]
                            1      1
                
    
    2 + 2 + 2 + 2 
    if 8 % 2 exists or == 0
                        8
                dp[]


    amount = 8, coins = [2,3]   
    
    dp[0] = 1
    for coin in coins:
            for x in range(coin, amount + 1):

    coin = 2

    range(2, 9)

    dp[2] += dp[2-2] = 1
    dp[3] += dp[3-2] = 0
    dp[4] += dp[4-2] = 1
    dp[5] += 

    """
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]

         









        