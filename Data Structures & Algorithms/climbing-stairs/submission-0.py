class Solution:
    def climbStairs(self, n: int) -> int:

        """
        no. ways to climb stairs taking 1 or 2 steps

        n=1 -> 1   {1}
        n=2 -> 2 : {1+1, 2}
        n=3 -> climbStairs(2) + climbStairs(1) = {1+1+1, 1+2, 2+1}
        n=4 -> 
        
        """

        a = 1
        b = 2
        
        if n==1:
            return a

        if n==2:
            return b

        for i in range(2,n):

            c = a+b
            a = b
            b = c

        return c


            
        