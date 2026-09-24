class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        """



        R:

        given:
            nums: List[int]

        coins for nums[i]: nums[i - 1] * nums[i] * nums[i + 1]

        if i-1 or i+1 out of bounds times by 1

        return max no. coins you can receive by bursting all ballons

        E:
        can we have negatives -> no
        wouldn't matter as we have to burst all ballons

        max size of nums (n): 300
        min n: 1

        if nums contains zero - return 0

        A:

        Input: nums = [4,2,3,7]

        Output: 143


        [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []

        

        [4,2,3,7] -> [4,2,7], [4,7],     7,    []
        2*3*7.    +   4*2*7  +  1*4*7 + 1*7*1  

        98+ 35 = 133 < 143

        

       


        dp[l][r] = max coins for that decision

        greedy approach of popping smallest number to allow bigger numbers to be multiplied with one another     ?    


        each step we ask, if I were to pop myself, what's max value u could get me?


        current state * the half of list 

        each column represents an elem, diagonal means pop

        4 2 3 7

         0 1 2 3
        [0,0,0,0]
        [0,0,0,0]
        [0,0,0,0]
        [0,0,0,0]


               1,4,2,3,7,1 
               l k       r

               func(l,k) +nums[l] * nums[k] * nums[r] + func(k,r)
               0 1 2 3 4 5
               
            1           4,2,3,7,1
            lr          l k     r  
            

                    4,2         2,3,7,1
                    l kr        l k   r

                             2,3    3,7,1
                             l,r      k
                                  3,7     7,1
                              0    0.      0

        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]


        def func(l,r):

            if l+1 == r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            best = 0
            for k in range(l+1, r):
                best = max(best,func(l,k) + nums[l] * nums[k] * nums[r] + func(k,r))
            

            dp[l][r] = best

            return dp[l][r]


        return func(0, n-1)







        